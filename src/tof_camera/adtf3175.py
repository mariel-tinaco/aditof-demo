import sys, os
import numpy as np
from pathlib import Path
from enum import Enum


sys.path.append(os.path.join(os.getcwd(), '.'))
import bin.aditofpython as tof

from .tof import TOFCamera, TOFCameraContext, MapType

CONFIG_PATH = Path(__file__).parent.parent.parent / 'config' / "tof-viewer_config.json"

class ModesEnum(Enum):
    MODE_NEAR = 0
    MODE_MEDIUM = 1
    MODE_FAR = 2

class ADTF3175Camera (TOFCamera):
    
    def __init__ (self, camera):
        self._camera = camera
        self.frame = None

        status = self._camera.setControl("initialization_config", str(CONFIG_PATH))
        if not status:
            print("camera.setControl()", status)

        status = self._camera.initialize() 
        if not status:
            print("camera.initialize() failed with status: ", status)

    def configure (self, configuration):
        try:
            status = self._camera.setMode(configuration['mode'])
            if not status:
                print("cameras[0].setMode() failed with status: ", status)

            status = self._camera.setFrameType(configuration['type']) # types[2] is 'mp_pcm' type.
            if not status:
                print("cameras[0].setFrameType() failed with status:", status)

        except:
            print("Failed")

    def start (self):
        status = self._camera.start()
        if not status:
            print("cameras[0].start() failed with status:", status)
    
        camDetails = tof.CameraDetails()
        status = self._camera.getDetails(camDetails)
        if not status:
            print("system.getDetails() failed with status: ", status)

        # Enable noise reduction for better results
        smallSignalThreshold = 100
        self._camera.setControl("noise_reduction_threshold", str(smallSignalThreshold))

        self.frame = tof.Frame()

    def stop (self):
        self._camera.stop()

    def request_frame (self):
        status = self._camera.requestFrame(self.frame)
        if not status:
            print("cameras[0].requestFrame() failed with status: ", status)
        return status, self.frame

    def get_bulk_frame (self):
        status = self._camera.requestFrame(self.frame)
        if not status:
            print("cameras[0].requestFrame() failed with status: ", status)

        ir_map = np.array(self.frame.getData('ir'), dtype="uint16", copy=False)
        depth_map = np.array(self.frame.getData('depth'), dtype="uint16", copy=False)
        
        return status, {'ir' : ir_map, 'depth' : depth_map}

    def fetch (self, datatype):
        # Capture frame-by-frame
        status = self._camera.requestFrame(self.frame)
        if not status:
            print("cameras[0].requestFrame() failed with status: ", status)

        map = np.array(self.frame.getData(datatype), dtype="uint16", copy=False)
        return status, map

    @property
    def camera (self):
        return self._camera

    @property
    def modes (self) -> list:
        _modes = []
        status = self._camera.getAvailableModes(_modes)
        if not status:
            print("system.getAvailableModes() failed with status: ", status)
        return _modes

    @property
    def frametypes (self) -> list:
        _types = []
        status = self._camera.getAvailableFrameTypes(_types)
        if not status:
            print("system.getAvailableFrameTypes() failed with status: ", status)
        return _types 

if __name__ == "__main__":

    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.use('tkagg')

    system = tof.System()

    ip = "10.42.0.1"

    cameras = []
    status = system.getCameraListAtIp(cameras, ip)
    if not status:
        print("system.getCameraList() failed with status: ", status)

    tofcam = TOFCameraContext (ADTF3175Camera(cameras[0]))

    print(tofcam.dev_id)

    cam_modes = tofcam.camera.modes 
    frame_types = tofcam.camera.frametypes

    config = {
        'mode' : cam_modes[ModesEnum.MODE_NEAR.value],
        'type' : frame_types[0]
    }

    tofcam.configure(config)
    image = tofcam.snapshot(MapType.IR.value)

    plt.figure()
    plt.imshow(image)
    plt.colorbar()
    plt.show()
