from PySide6 import QtWidgets, QtCore, QtGui

from ..tof_camera.adtf3175 import ADTF3175Camera
from ..tof_camera.tof import TOFCameraContext, TOFCamera

import bin.aditofpython as tof

IP = "10.42.0.1"

class ToFController (QtCore.QObject):

    def __init__ (self):
        super(ToFController, self).__init__()

        self.available_cameras = []

    def initialize (self):

        # Initialize ToF Cameras
        self.system = tof.System()
        aditofcameras = []
        status = self.system.getCameraListAtIp(aditofcameras, IP)
        if not status:
            print("system.getCameraList() failed with status: ", status)

        for aditofcamera in aditofcameras:
            self.available_cameras.append(TOFCameraContext(ADTF3175Camera(aditofcamera)))

        # Initialize Azure Kinect





if __name__ == "__main__":

    tofctrl = ToFController()
    tofctrl.initialize()

    