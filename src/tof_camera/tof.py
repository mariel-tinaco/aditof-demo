

from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from typing import Tuple
from collections import namedtuple
import numpy as np

class MapType (Enum):
    DEPTH = 'depth'
    IR = 'ir'

Frame = namedtuple('Frame', ['ir', 'depth'])

class TOFCamera (ABC):

    @abstractmethod
    def configure (self, configuration):
        raise NotImplementedError

    @abstractmethod
    def start (self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
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

    def cameraDetails (self):
        return self._camera.camDetails

    def configure (self, configuration):
        try:
            self._camera.configure (configuration)
        except:
            raise SystemError ("Configuration Error")

    def start (self):
        self._camera.start()

    def read (self) -> Tuple[bool, Frame]:
        status, frame = self._camera.request_frame()
        return status, frame

    def snapshot (self, datatype):
        self._camera.start()
        status, image = self._camera.fetch(datatype)
        self._camera.stop()
        if status:
            return image
        else:
            raise IOError("Unable to fetch frame")

    def read_bulk (self):
        self._camera.start()
        status, frames = self._camera.get_bulk_frame()
        self._camera.stop()
        return status, frames

    def stream_bulk (self):
        self._camera.start()
        status, frames = self._camera.get_bulk_frame()
        return status, frames

    def stop (self):
        self._camera.stop()