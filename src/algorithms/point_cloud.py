import sys, os
import numpy as np
from pathlib import Path
import cv2 as cv
import open3d as o3d

from .tof_algo import TofAlgorithm

class PointCloud (TofAlgorithm):
    camera_range = 5000
    bitCount = 9


    def __init__ (self):
        
        self.width = 0
        self.height = 0
        self._camDetails = None

    @property
    def camDetails (self):
        return self._camDetails

    @camDetails.setter
    def camDetails (self, data):
        self._camDetails = data

    def convert (self, depth_map, ir_map):
        # Get intrinsic parameters from camera

        intrinsicParameters = self._camDetails.intrinsics
        fx = intrinsicParameters.fx
        
        fy = intrinsicParameters.fy
        
        cx = intrinsicParameters.cx

        cy = intrinsicParameters.cy
        
        cameraIntrinsics = o3d.camera.PinholeCameraIntrinsic(self.width, self.height, fx, fy, cx, cy)
        
        max_value_of_IR_pixel = 2 ** self.bitCount - 1
        distance_scale_ir = 255.0 / max_value_of_IR_pixel
        distance_scale = 255.0 / self.camera_range

        # Create the IR imageq
        new_shape = (int(ir_map.shape[0]),int(ir_map.shape[1]))
        ir_map = ir_map = np.resize(ir_map,new_shape)
        ir_map = distance_scale_ir * ir_map
        ir_map = np.uint8(ir_map)
        ir_map = cv.cvtColor(ir_map, cv.COLOR_GRAY2RGB)
        # print (ir_map.shape)

        # Create the Depth image
        new_shape = (int(depth_map.shape[0]), int(depth_map.shape[1]))
        depth16bits_map = depth_map = np.resize(depth_map, new_shape)
        depth_map = distance_scale * depth_map
        depth_map = np.uint8(depth_map)
        depth_map = cv.applyColorMap(depth_map, cv.COLORMAP_RAINBOW)
        # cv.imwrite("DEPTH.png",depth_map)
        
        img_color = cv.absdiff(ir_map, depth_map)

        color_image = o3d.geometry.Image(img_color)
        # print (f"color_image is {color_image}")
        depth16bits_image = o3d.geometry.Image(depth_map)
        #75.0 , 3 ---> Best ---> 87.5
        # rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_image, depth16bits_image, 750.0 , 100, True)
        rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_image, depth16bits_image, 1.0 , 100, True)

        pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, cameraIntrinsics )

        # return [np.array(rgbd_image.depth), img_color]
        return [np.array(rgbd_image.depth), np.array(color_image)]