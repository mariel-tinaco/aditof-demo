import numpy as np
import cv2
import sys, os
from abc import ABC, abstractmethod
from pathlib import Path

class TofAlgorithm (ABC):

    @abstractmethod
    def convert (self, depth_map, ir_map) -> np.ndarray:
        raise NotImplementedError


class TofAlgorithmContext:

    def __init__ (self, algorithm : TofAlgorithm = None):
        self._algorithm = algorithm

    @property
    def algorithm (self):
        return self._algorithm

    @algorithm.setter
    def algorithm (self, alg):
        self._algorithm = alg


    def process_frames (self, *args, **kwargs):
        return self._algorithm.convert(*args, **kwargs)


class BaselineTof (TofAlgorithm):

    def __init__ (self, *args, **kwargs):
        super().__init__()

        camera_range = 5000
        bitCount = 9

        max_value_of_IR_pixel = 2 ** bitCount - 1
        self.distance_scale_ir = 255.0 / max_value_of_IR_pixel
        self.distance_scale = 255.0 / camera_range

    def convert (self, depth_map, ir_map):

        # Creation of the IR image
        # ir_map = ir_map[0: int(ir_map.shape[0] / 2), :]
        ir_map = self.distance_scale_ir * ir_map
        ir_map = np.uint8(ir_map)
        ir_map = cv2.flip(ir_map, 1)
        ir_map = cv2.cvtColor(ir_map, cv2.COLOR_GRAY2RGB)

        # Creation of the Depth image
        # new_shape = (int(depth_map.shape[0] / 2), depth_map.shape[1])
        # depth_map = np.resize(depth_map, new_shape)
        depth_map = cv2.flip(depth_map, 1)
        distance_map = depth_map
        depth_map = self.distance_scale * depth_map
        depth_map = np.uint8(depth_map)
        depth_map = cv2.applyColorMap(depth_map, cv2.COLORMAP_RAINBOW)

        return [depth_map, ir_map]