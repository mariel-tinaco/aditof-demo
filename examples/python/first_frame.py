#
# BSD 3-Clause License
#
# Copyright (c) 2019, Analog Devices, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# ADDITIONAL EDITS TO MAKE THE CODE WORK
# 1. Changed importing of python bindings
# 2. Added lines 41 and 42 that changes the matplotlib-qt backend to be compatible with PySide6
#       Ref: https://stackoverflow.com/questions/74112099/importing-matplotlib-causes-int-argument-must-be-a-string-error
# 3. Placed .json, .ini, and .cfg config files in config directory
# 4. Changed FrameType from lrqmp to qmp
# 5. For the following error:
#       I1027 20:15:18.145859 14028 camera_itof.cpp:695] initComputeLibrary
#       Failed to open data file C:\Users\MTinaco\AppData\Local\Programs\Python\Python39\tofi_processor.obj.
#       Failed to load the compute engine
#       Failed to initialize OpenCL config
#       Failed to initialize TOFI Processor Config
#   The only work around is to provide the .obj file on the root Python dir. Ongoing investigation

import numpy as np
import matplotlib.pyplot as plt
import sys, os
from pathlib import Path

import matplotlib
matplotlib.use('tkagg')

sys.path.append(os.path.join(os.getcwd(), '.'))
import bin.aditofpython as tof


# if len(sys.argv) < 2  or sys.argv[1] == "--help" or sys.argv[1] == "-h" :
#     print("first_frame.py usage:")
#     print("USB / Local connection: first_frame.py <config>")
#     print("Network connection: first_frame.py <ip> <config>")
#     exit(1)

system = tof.System()

# cameras = []
# if len(sys.argv) == 3 :
#     status = system.getCameraListAtIp(cameras,sys.argv[1])
#     config = sys.argv[2]
# elif len(sys.argv) == 2 :
#     status = system.getCameraList(cameras)
#     config = sys.argv[1]
# else :
#     print("Too many arguments provided!")
#     exit(1)

config = Path(__file__).parent.parent.parent / 'config' / "tof-viewer_config.json"
ip = "10.42.0.1"

cameras = []
status = system.getCameraListAtIp(cameras, ip)
if not status:
    print("system.getCameraList() failed with status: ", status)

status = cameras[0].setControl("initialization_config", str(config))
if not status:
    print("camera[0].setControl()", status)

camera1 = cameras[0]

status = camera1.initialize()
print("camera1.initialize()", status)

types = []
status = camera1.getAvailableFrameTypes(types)
print("camera1.getAvailableFrameTypes()", status)
print(types)

camDetails = tof.CameraDetails()
status = camera1.getDetails(camDetails)
print("camera1.getDetails()", status)
print("camera1 details:", "id:", camDetails.cameraId, "connection:", camDetails.connection)

status = camera1.setFrameType("mp")
print("camera1.setFrameType()", status)
# print("lrqmp")
print("qmp")

status = camera1.start()
print("camera1.start()", status)

frame = tof.Frame()
status = camera1.requestFrame(frame)
print("camera1.requestFrame()", status)

frameDataDetails = tof.FrameDataDetails()
status = frame.getDataDetails("depth", frameDataDetails)
print("frame.getDataDetails()", status)
print("depth frame details:", "width:", frameDataDetails.width, "height:", frameDataDetails.height, "type:", frameDataDetails.type)

image = np.array(frame.getData("depth"), copy=False)

camera1.stop()





if __name__ == "__main__":
    from PySide6 import QtWidgets, QtCore, QtGui
    import cv2

    class Window (QtWidgets.QWidget):

        def __init__ (self, image):
            super().__init__()

            layout = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel()
            grayframe = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            h, w = image.shape[:2]
            bytesPerLine = 3*w
            qimage = QtGui.QImage(grayframe.data, w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            qpixmap = QtGui.QPixmap.fromImage(qimage).scaled(h, w)

            label.setPixmap(qpixmap)
            layout.addWidget(label)
            self.setLayout(layout)

    app = QtWidgets.QApplication(sys.argv)
    widget = Window(image)
    widget.show()
    sys.exit(app.exec())

# plt.figure()
# plt.imshow(image)
# plt.colorbar()
# plt.show()


