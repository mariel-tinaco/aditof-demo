import numpy as np
import sys, os
import time
from PySide6 import QtWidgets, QtCore, QtGui
import qimage2ndarray

from src.tof_camera.tof import TOFCameraContext, Frame
from src.tof_camera.adtf3175 import ADTF3175Camera
from src.algorithms.tof_algo import BaselineTof, TofAlgorithmContext
from src.algorithms.dnn_object_detect import DNNObjectDetection

import bin.aditofpython as tof

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
        self.source.start()
        while self.runs:
            status, frames = self.source.read()
            if status:
                # self.changeFrame.emit(qpixmap)
                self.callback(frames)

class Widget (QtWidgets.QWidget):

    sigCap = QtCore.Signal(np.ndarray)

    def __init__ (self):
        super().__init__ ()

        layout = QtWidgets.QVBoxLayout()
        self.startbtn = QtWidgets.QPushButton("Start")
        self.stopbtn = QtWidgets.QPushButton("Stop")
        self.piclabel = QtWidgets.QLabel()

        layout.addWidget(self.startbtn)
        layout.addWidget(self.stopbtn)
        layout.addWidget(self.piclabel)
        
        # self.startbtn.clicked.connect(self.start_stream)
        self.startbtn.clicked.connect(self.start_stream)
        self.stopbtn.clicked.connect(self.stop_stream)

        adtf_system = tof.System()
        aditofcameras = []
        status = adtf_system.getCameraListAtIp(aditofcameras, "10.42.0.1")
        if not status:
            print("system.getCameraList() failed with status: ", status)
            raise SystemError("Initialization Error")

        self.camera = TOFCameraContext(ADTF3175Camera(aditofcameras[0]))
        # self.algo = TofAlgorithmContext(BaselineTof())
        self.algo = TofAlgorithmContext(DNNObjectDetection())

        self.setLayout(layout)
        
        # self.sigCap.connect(self.update_frame)

    def frame_display_callback (self, frames):
        baseframes = self.algo.process_frames(frames.depth, frames.ir)
        frame = baseframes[1]
        h, w = frame.shape[:2]
        bytesPerLine = 3*w
        qimage = QtGui.QImage(frame.data, w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
        qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)
        self.piclabel.setPixmap(qpixmap)


    @QtCore.Slot(np.ndarray)
    def update_frame (self, qpixmap):
        # image = qimage2ndarray.array2qimage(frame)
        # self.piclabel.setPixmap(QtGui.QPixmap.fromImage(image))
        self.piclabel.setPixmap(qpixmap)

    @QtCore.Slot()
    def capture (self):
        cam_modes = self.camera.camera.modes 
        frame_types = self.camera.camera.frametypes
        configuration = {
            'mode' : cam_modes[0],
            'type' : frame_types[0]
        }

        self.camera.configure(configuration)
        # self.camera.start()
        status, frames = self.camera.read_bulk()
        self.sigCap.emit(frames)

    @QtCore.Slot()
    def start_stream (self):
        self.th = StreamHandler(self.camera, self.frame_display_callback)
        # self.th.changeFrame.connect(self.update_frame)
        
        def delete_thread ():
            del self.th

        self.th.finished.connect(delete_thread)

        cam_modes = self.camera.camera.modes 
        frame_types = self.camera.camera.frametypes
        configuration = {
            'mode' : cam_modes[0],
            'type' : frame_types[0]
        }

        self.camera.configure(configuration)
        self.th.runs = True
        self.th.start()

    @QtCore.Slot()
    def stop_stream (self):
        self.camera.stop()
        self.th.runs = False
        self.th.exit()
        # self.th.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = Widget()
    win.show()
    sys.exit(app.exec())


    

