import cv2
import sys, os
import numpy as np
from pathlib import Path
from .tof_algo import TofAlgorithm

class DNNObjectDetection (TofAlgorithm):

    prototxt = Path(__file__).parent.parent.parent / 'assets' / 'MobileNetSSD_deploy.prototxt'
    weights = Path(__file__).parent.parent.parent / 'assets' / 'MobileNetSSD_deploy.caffemodel'
    inWidth = 300
    inHeight = 300
    WHRatio = inWidth / float(inHeight)
    inScaleFactor = 0.007843
    meanVal = 127.5
    thr = 0.2

    def __init__ (self, *args, **kwargs):
        try:
            self.net = cv2.dnn.readNetFromCaffe(str(self.prototxt), str(self.weights))
        except:
            print("Error: Please give the correct location of the prototxt and caffemodel")
            sys.exit(1)
        
        self.swapRB = False
        self.classNames = {0: 'background',
            1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
            5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
            10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
            14: 'motorbike', 15: 'person', 16: 'pottedplant',
            17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor'}

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

        # Combine depth and IR for more accurate results
        result = cv2.addWeighted(ir_map, 0.4, depth_map, 0.6, 0)

        # Start the computations for object detection using DNN
        blob = cv2.dnn.blobFromImage(result, self.inScaleFactor, (self.inWidth, self.inHeight), (self.meanVal, self.meanVal, self.meanVal), self.swapRB)
        
        self.net.setInput(blob)
        detections = self.net.forward()

        cols = result.shape[1]
        rows = result.shape[0]

        if cols / float(rows) > self.WHRatio:
            cropSize = (int(rows * self.WHRatio), rows)
        else:
            cropSize = (cols, int(cols / self.WHRatio))

        y1 = int((rows - cropSize[1]) / 2)
        y2 = y1 + cropSize[1]
        x1 = int((cols - cropSize[0]) / 2)
        x2 = x1 + cropSize[0]
        result = result[y1:y2, x1:x2]
        depth_map = depth_map[y1:y2, x1:x2]
        distance_map = distance_map[y1:y2, x1:x2]

        cols = result.shape[1]
        rows = result.shape[0]

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > self.thr:
                class_id = int(detections[0, 0, i, 1])
                xLeftBottom = int(detections[0, 0, i, 3] * cols)
                yLeftBottom = int(detections[0, 0, i, 4] * rows)
                xRightTop = int(detections[0, 0, i, 5] * cols)
                yRightTop = int(detections[0, 0, i, 6] * rows)

                cv2.rectangle(result, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
                             (0, 255, 0))
                cv2.rectangle(depth_map, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
                             (0, 255, 0))
                center = ((xLeftBottom + xRightTop) * 0.5, (yLeftBottom + yRightTop) * 0.5)

                value_x = int(center[0])
                value_y = int(center[1])
                cv2.drawMarker(result, (value_x, value_y), (0, 0, 0), cv2.MARKER_CROSS)
                cv2.drawMarker(depth_map, (value_x, value_y), (0, 0, 0), cv2.MARKER_CROSS)

                if class_id in self.classNames:
                    label_depth = self.classNames[class_id] + ": " + \
                            "{0:.3f}".format(distance_map[value_x, value_y] / 1000.0) + " meters"
                    label_conf = "Confidence: " + "{0:.4f}".format(confidence)
                    labelSize_depth, baseLine = cv2.getTextSize(label_depth, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                    labelSize_conf = cv2.getTextSize(label_conf, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

                    if labelSize_depth[1] > labelSize_conf[1]:
                        labelSize = labelSize_depth
                    else:
                        labelSize = labelSize_conf
                    yLeftBottom = max(yLeftBottom, labelSize[1])
                    cv2.rectangle(result, (value_x - int(labelSize[0] * 0.5), yLeftBottom),
                                 (value_x + int(labelSize[0] * 0.5), yLeftBottom + 2 * labelSize[1] + 2 * baseLine),
                                 (255, 255, 255), cv2.FILLED)
                    cv2.putText(result, label_depth, (value_x - int(labelSize[0] * 0.5), yLeftBottom + labelSize[1]),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
                    cv2.putText(result, label_conf, (value_x - int(labelSize[0] * 0.5), yLeftBottom + 2 * labelSize[1]
                                                    + baseLine),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

                    cv2.rectangle(depth_map, (value_x - int(labelSize[0] * 0.5), yLeftBottom),
                                 (value_x + int(labelSize[0] * 0.5), yLeftBottom + 2 * labelSize[1] + 2 * baseLine),
                                 (255, 255, 255), cv2.FILLED)
                    cv2.putText(depth_map, label_depth, (value_x - int(labelSize[0] * 0.5),  yLeftBottom + labelSize[1]),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
                    cv2.putText(depth_map, label_conf, (value_x - int(labelSize[0] * 0.5), yLeftBottom + 2 * labelSize[1]
                                                       + baseLine),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

            return [result, depth_map]