from PySide6 import QtWidgets, QtCore, QtGui
import numpy as np
from enum import Enum

from ..tof_camera.adtf3175 import ADTF3175Camera
from ..tof_camera.tof import TOFCameraContext, TOFCamera

from ..algorithms.tof_algo import TofAlgorithmContext, BaselineTof
from ..algorithms.dnn_object_detect import DNNObjectDetection
from ..algorithms.point_cloud import PointCloud
from ..algorithms.body_tracking import BodyTracking

import bin.aditofpython as tof

IP = "10.42.0.1"

class TofAlgorithmMode(Enum):
    BASE = 0
    DNN = 1
    POINTCLOUD = 2
    SKELETON = 3

class ToFController (QtCore.QObject):

    def __init__ (self):
        super(ToFController, self).__init__()

        self.available_cameras = []
        self.current_camera = None

        self.alg_select = {
            TofAlgorithmMode.BASE : BaselineTof(),
            TofAlgorithmMode.DNN : DNNObjectDetection(),
            TofAlgorithmMode.POINTCLOUD : PointCloud(),
            TofAlgorithmMode.SKELETON : BodyTracking()
        }


    def initialize (self):

        # Initialize ToF Cameras
        adtf_system = tof.System()
        aditofcameras = []
        status = adtf_system.getCameraListAtIp(aditofcameras, IP)
        if not status:
            print("system.getCameraList() failed with status: ", status)
            raise SystemError("Initialization Error")

        for aditofcamera in aditofcameras:
            self.available_cameras.append(TOFCameraContext(ADTF3175Camera(aditofcamera)))

        # Initialize Azure Kinect

    def getCameraDetails (self):
        camera = self.current_camera.cameraDetails()
        return camera

    def getWidth (self):
        return self.current_camera.camera.imgWidth

    def getHeight (self):
        return self.current_camera.camera.imgHeight

    def configure (self, configuration : dict):
        self.current_camera.configure(configuration)
        # self.stream_handler = StreamHandler(self.current_camera)

    def capture (self):
        status, bulk_frames = self.current_camera.read_bulk()
        return status, bulk_frames

    def fetch (self):
        status, bulk_frames = self.current_camera.stream_bulk()
        return status, bulk_frames

    def get_algo (self, mode):
        return TofAlgorithmContext(self.alg_select[mode])

    def stop_stream (self):
        self.stream_handler.wait()
        self.current_camera.stop()

if __name__ == "__main__":

    tofctrl = ToFController()
    tofctrl.initialize()

    