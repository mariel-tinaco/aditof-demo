from PySide6 import QtWidgets, QtCore, QtGui
from ..tof_camera.tof import TOFCameraContext
from ..algorithms.tof_algo import TofAlgorithmContext, BaselineTof
from ..algorithms.dnn_object_detect import DNNObjectDetection
from ..algorithms.body_tracking import BodyTracking
from ..algorithms.point_cloud import PointCloud
from src.controllers.tofcontroller import ToFController, TofAlgorithmMode
import qimage2ndarray
import cv2
import numpy as np

class StreamHandler (QtCore.QThread):

    changeFrame = QtCore.Signal(np.ndarray)

    def __init__ (self, source : TOFCameraContext, callback = None):
        super().__init__()
        if source:
            self.source = source
        else:
            raise IOError("Provide Camera source")
        
        self.callback = callback
        self.runs = False

    def run (self):
        while self.runs:
            status, frames = self.source.read()
            if status:
                # self.changeFrame.emit(qpixmap)
                self.callback(frames)

class MainController (QtCore.QObject):

    signalLog = QtCore.Signal(str)

    def __init__(self, view, model):
        super(MainController, self).__init__()

        self.view = view
        self.model = model
        self.tofctrl = ToFController()

        self.view.listWidget.setCurrentRow(0)

    def connect_signals (self):
        # View signals
        self.view.signalRefresh.connect(self.refresh)
        # self.view.signalConfigure.connect(self.configure)
        self.view.signalPlay.connect(self.stream)
        self.view.signalPause.connect(self.stop)
        self.view.signalCapture.connect(self.capture)

        # Controller signals
        self.signalLog.connect(self.view.log)

    @QtCore.Slot()
    def refresh (self):
        self.tofctrl.initialize()
        toflist = [cam.dev_id for cam in self.tofctrl.available_cameras]
        self.view.setCameraOptions(toflist)

    @QtCore.Slot()
    def configure (self):
        camselect = self.view.cameracombobox.currentIndex()
        tofcam = self.tofctrl.available_cameras[camselect]
        cam_modes = tofcam.camera.modes 
        frame_types = tofcam.camera.frametypes
        configuration = {
            'mode' : cam_modes[0],
            'type' : frame_types[0]
        }
        
        self.tofctrl.current_camera = tofcam
        self.tofctrl.configure(configuration)
        # self.tofctrl.stream_handler.changeFrame.connect(self.display_frame)

        # self.view.signalCapture.emit()
        
    def frame_display_callback (self, frames):
        current_algo = self.view.listWidget.currentRow()

        if current_algo == 0:
            algo = TofAlgorithmContext(BaselineTof())
            baseframes = algo.process_frames(frames.depth, frames.ir)
            ir_frame = baseframes[1]
            depth_frame = baseframes[0]

            h, w = ir_frame.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(ir_frame.data, w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.irpixmaplabel.setPixmap(qpixmap)

            h, w = depth_frame.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(depth_frame.data, w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.depthpixmaplabel.setPixmap(qpixmap)
        
        elif current_algo == 1:
            algo = TofAlgorithmContext(DNNObjectDetection())

            dnnframes = algo.process_frames(frames.depth, frames.ir)
            dnn_result = dnnframes[0]
            dnn_depth_map = dnnframes[1]

            # rgb = cv2.cvtColor(bulkframes['ir'],cv2.COLOR_GRAY2RGB)
            h, w = dnn_result.shape[:2]
            # bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(dnn_result), w, h, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.dnnpixmaplabel.setPixmap(qpixmap)
            
            # # rgb = cv2.cvtColor(bulkframes['depth'],cv2.COLOR_GRAY2RGB)
            h, w = dnn_depth_map.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(dnn_depth_map), w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.dnndepthpixmaplabel.setPixmap(qpixmap)

        elif current_algo == 2:

            algo = TofAlgorithmContext(PointCloud())
            algo.algorithm.camDetails = self.camDetails
            algo.algorithm.width = self.tofctrl.getWidth()
            algo.algorithm.height = self.tofctrl.getHeight()

            pcdframes = algo.process_frames(frames.depth, frames.ir)
            pcd_depth = pcdframes[0]
            pcd_points = pcdframes[1]

            h, w = pcd_depth.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(pcd_depth), w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)

            self.view.pcddepthpixmaplabel.setPixmap(qpixmap)

            h, w = pcd_points.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(pcd_points), w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)

            self.view.pcdpointspixmaplabel.setPixmap(qpixmap)

        elif current_algo == 3:

            algo = TofAlgorithmContext(BodyTracking())

            skelframes = algo.process_frames(frames.depth, frames.ir)
            skelresult = skelframes[0]

            h, w = skelresult.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(skelresult), w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.bodytrackingirpixmaplabel.setPixmap(qpixmap)

    @QtCore.Slot()
    def stream (self):

        camselect = self.view.cameracombobox.currentIndex()
        tofcam = self.tofctrl.available_cameras[camselect]

        self.th = StreamHandler(tofcam, self.frame_display_callback)
        # self.th.changeFrame.connect(self.update_frame)
        
        def delete_thread ():
            del self.th

        self.th.finished.connect(delete_thread)

        cam_modes = tofcam.camera.modes 
        frame_types = tofcam.camera.frametypes
        configuration = {
            'mode' : cam_modes[0],
            'type' : frame_types[0]
        }
        
        self.tofctrl.current_camera = tofcam
        self.tofctrl.configure(configuration)
        self.tofctrl.current_camera.start()
        
        self.camDetails = self.tofctrl.getCameraDetails()

        self.th.runs = True
        self.th.start()

    @QtCore.Slot()
    def stop(self):
        self.tofctrl.current_camera.stop()
        self.th.runs = False
        self.th.exit()        

    def display_frame (self, frame):

        bulkframes = frame

        currentMode = TofAlgorithmMode(self.view.listWidget.currentRow())
        algo = self.tofctrl.get_algo(currentMode)

        if currentMode == TofAlgorithmMode.BASE:
            baseframes = algo.process_frames(bulkframes.depth, bulkframes.ir)
            ir_map = baseframes[1]
            depth_map = baseframes[0]

            image = qimage2ndarray.array2qimage(ir_map)
            self.view.irpixmaplabel.setPixmap(QtGui.QPixmap.fromImage(image))
            
            image = qimage2ndarray.array2qimage(depth_map)
            self.view.depthpixmaplabel.setPixmap(QtGui.QPixmap.fromImage(image))

        elif currentMode == TofAlgorithmMode.DNN:
            dnnframes = algo.process_frames(bulkframes.depth, bulkframes.ir)
            dnn_result = dnnframes[0]
            dnn_depth_map = dnnframes[1]

            image = qimage2ndarray.array2qimage(dnn_result)
            self.view.dnnpixmaplabel.setPixmap(QtGui.QPixmap.fromImage(image))
        
            image = qimage2ndarray.array2qimage(dnn_depth_map)
            self.view.dnndepthpixmaplabel.setPixmap(QtGui.QPixmap.fromImage(image))

        elif currentMode == TofAlgorithmMode.SKELETON:
            algo = TofAlgorithmContext(BodyTracking())

            skelframes = algo.process_frames(bulkframes.depth, bulkframes.ir)
            skelresult = skelframes[0]

            h, w = skelresult.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(skelresult), w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.bodytrackingirpixmaplabel.setPixmap(qpixmap)

    @QtCore.Slot()
    def capture (self):
        camselect = self.view.cameracombobox.currentIndex()
        tofcam = self.tofctrl.available_cameras[camselect]
        cam_modes = tofcam.camera.modes 
        frame_types = tofcam.camera.frametypes
        configuration = {
            'mode' : cam_modes[0],
            'type' : frame_types[0]
        }
        
        self.tofctrl.current_camera = tofcam
        self.tofctrl.configure(configuration)

        status, bulkframes = self.tofctrl.capture()
        
        self.camDetails = self.tofctrl.getCameraDetails()

        baseline_algo = self.tofctrl.get_algo(TofAlgorithmMode.BASE)
        dnn_algo = self.tofctrl.get_algo(TofAlgorithmMode.DNN)
        pcd_algo = self.tofctrl.get_algo(TofAlgorithmMode.POINTCLOUD)
        skel_algo = self.tofctrl.get_algo(TofAlgorithmMode.SKELETON)

        if status:

            baseframes = baseline_algo.process_frames(bulkframes['depth'], bulkframes['ir'])
            ir_map = baseframes[1]
            depth_map = baseframes[0]

            # rgb = cv2.cvtColor(bulkframes['ir'],cv2.COLOR_GRAY2RGB)
            h, w = ir_map.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(ir_map.data, w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.irpixmaplabel.setPixmap(qpixmap)
            
            # rgb = cv2.cvtColor(bulkframes['depth'],cv2.COLOR_GRAY2RGB)
            h, w = depth_map.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(depth_map.data, w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.depthpixmaplabel.setPixmap(qpixmap)
            
            dnnframes = dnn_algo.process_frames(bulkframes['depth'], bulkframes['ir'])
            dnn_result = dnnframes[0]
            dnn_depth_map = dnnframes[1]

            # rgb = cv2.cvtColor(bulkframes['ir'],cv2.COLOR_GRAY2RGB)
            h, w = dnn_result.shape[:2]
            # bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(dnn_result), w, h, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.dnnpixmaplabel.setPixmap(qpixmap)
            
            # # rgb = cv2.cvtColor(bulkframes['depth'],cv2.COLOR_GRAY2RGB)
            h, w = dnn_depth_map.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(dnn_depth_map), w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.dnndepthpixmaplabel.setPixmap(qpixmap)

            pcd_algo.algorithm.camDetails = self.camDetails
            pcd_algo.algorithm.width = self.tofctrl.getWidth()
            pcd_algo.algorithm.height = self.tofctrl.getHeight()

            pcd_frames = pcd_algo.process_frames(bulkframes['depth'], bulkframes['ir'])
            pcd_depth = pcd_frames[0]
            pcd_points = pcd_frames[1]

            h, w = pcd_depth.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(pcd_depth), w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.pcddepthpixmaplabel.setPixmap(qpixmap)

            h, w = pcd_points.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(pcd_points), w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)

            self.view.pcdpointspixmaplabel.setPixmap(qpixmap)

            skelframes = skel_algo.process_frames(bulkframes['depth'], bulkframes['ir'])
            skelresult = skelframes[0]

            h, w = skelresult.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(bytes(skelresult), w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.bodytrackingirpixmaplabel.setPixmap(qpixmap)


    def start (self):
        self.view.show()


