

from abc import ABC, abstractmethod
from enum import Enum

import numpy as np

class MapType (Enum):
    DEPTH = 'depth'
    IR = 'ir'

class TOFCamera (ABC):

    @abstractmethod
    def configure (self, configuration):
        raise NotImplementedError

    @abstractmethod
    def start (self):
        raise NotImplementedError

    @abstractmethod
    def fetch (self):
        raise NotImplementedError

    @abstractmethod
    def request_frame (self):
        raise NotImplementedError

class TOFCameraContext :

    def __init__ (self, camera : TOFCamera):
        self._camera = camera

    @property
    def camera (self):
        return self._camera

    @property
    def dev_id (self):
        return self._camera.__class__.__name__

    def configure (self, configuration):
        self._camera.configure (configuration)

    def snapshot (self, datatype):
        self._camera.start()
        status, image = self._camera.fetch(datatype)
        if status:
            self._camera.stop()
            return image
        else:
            raise IOError("Unable to fetch frame")

    def read (self):
        status, frame_object = self._camera.request_frame()
        return status, frame_object

    def read_bulk (self):
        self._camera.start()
        status, frames = self._camera.get_bulk_frame()
        self._camera.stop()
        return status, frames