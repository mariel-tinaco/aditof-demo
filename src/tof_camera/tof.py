

from abc import ABC, abstractmethod

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

    def configure (self, configuration):
        self._camera.configure (configuration)

    def snapshot (self):
        self._camera.start()
        return self._camera.fetch()
