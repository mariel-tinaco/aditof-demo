from PySide6 import QtWidgets, QtCore, QtGui

from src.controllers.tofcontroller import ToFController
import qimage2ndarray
import cv2
import numpy as np
class MainController (QtCore.QObject):

    def __init__(self, view, model):
        super(MainController, self).__init__()

        self.view = view
        self.model = model
        self.tofctrl = ToFController()

    def connect_signals (self):
        self.view.signalRefresh.connect(self.refresh)
        self.view.signalConfigure.connect(self.configure)
        self.view.signalPlay.connect(self.stream)
        self.view.signalPause.connect(self.stop)

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

        status, bulkframes = self.tofctrl.capture()

        camera_range = 5000
        bitCount = 9

        max_value_of_IR_pixel = 2 ** bitCount - 1
        distance_scale_ir = 255.0 / max_value_of_IR_pixel
        distance_scale = 255.0 / camera_range

        if status:
            
            ir_map = bulkframes['ir']
            # ir_map = ir_map[0: int(ir_map.shape[0] / 2), :]
            ir_map = distance_scale_ir * ir_map
            ir_map = np.uint8(ir_map)
            ir_map = cv2.flip(ir_map, 1)
            ir_map = cv2.cvtColor(ir_map, cv2.COLOR_GRAY2RGB)

            # rgb = cv2.cvtColor(bulkframes['ir'],cv2.COLOR_GRAY2RGB)
            h, w = ir_map.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(ir_map.data, w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.irpixmaplabel.setPixmap(qpixmap)
            
            depth_map = bulkframes['depth']
            depth_map = cv2.flip(depth_map, 1)
            distance_map = depth_map
            depth_map = distance_scale * depth_map
            depth_map = np.uint8(depth_map)
            depth_map = cv2.applyColorMap(depth_map, cv2.COLORMAP_RAINBOW)

            # rgb = cv2.cvtColor(bulkframes['depth'],cv2.COLOR_GRAY2RGB)
            h, w = depth_map.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(depth_map.data, w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
            self.view.depthpixmaplabel.setPixmap(qpixmap)
            

    @QtCore.Slot()
    def stream (self):
        print("streaming")

    @QtCore.Slot()
    def stop(self):
        print("stopping")

    def start (self):
        self.view.show()


