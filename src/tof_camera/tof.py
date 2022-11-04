

from abc import ABC, abstractmethod
from enum import Enum

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
        image = self._camera.fetch(datatype)
        self._camera.stop()
        return image