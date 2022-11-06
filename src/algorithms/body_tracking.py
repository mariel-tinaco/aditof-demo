import cv2 as cv
import sys, os
import numpy as np
import mediapipe as mp
from pathlib import Path
from .tof_algo import TofAlgorithm

class BodyTracking (TofAlgorithm):
    camera_range = 5000
    bitCount = 5

    max_value_of_IR_pixel = 2 ** bitCount - 1
    distance_scale_ir = 255.0 / max_value_of_IR_pixel
    distance_scale = 255.0 / camera_range

    def __init__ (self):
        super().__init__()
        #Initialize pipe
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose

        self.pose = self.mp_pose.Pose(min_detection_confidence = 0.5 , min_tracking_confidence = 0.5)

    def convert (self, depth_map, ir_map):
        
        new_shape = (int(depth_map.shape[0]), int(depth_map.shape[1]))
        depth16bits_map = depth_map = np.resize(depth_map, new_shape)
        depth_map = (self.distance_scale) * depth_map
        depth_map = np.uint8(depth_map)
        depth_map = cv.cvtColor(depth_map, cv.COLOR_GRAY2RGB)

        new_shape = (int(ir_map.shape[0]),int(ir_map.shape[1]))
        ir_map = np.resize(ir_map,new_shape)
        # ir_map = (distance_scale_ir*16) * ir_map
        # ir_map = np.uint16(ir_map)
        ir_map = self.distance_scale * ir_map 
        ir_map = np.uint8(ir_map)
        # ir_map = cv.flip(ir_map, 1)
        ir_map = cv.cvtColor(ir_map, cv.COLOR_GRAY2RGB)

        image = cv.addWeighted (ir_map , 0.4 , depth_map , 0.6 , 0)

        # image = cv.cvtColor(depth_map, cv.COLOR_GRAY2RGB)
        image.flags.writeable = False
        
        results = self.pose.process(image)

        image.flags.writeable = True
        image = cv.cvtColor (image , cv.COLOR_RGB2BGR)

        self.mp_drawing.draw_landmarks(image , results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS,
                                self.mp_drawing.DrawingSpec(color = (255,255,255) , thickness = 2 , circle_radius = 2), #dots
                                self.mp_drawing.DrawingSpec(color = (255,255,255) , thickness = 2 , circle_radius = 2) #lines
                                )
        
        return [image]