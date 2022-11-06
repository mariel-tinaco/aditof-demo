
from PySide6 import QtWidgets, QtGui,QtCore
import open3d as o3d
import win32gui
import sys
import threading
import time

class Worker(QtCore.QObject):
    def run(self,vis):
        vis.run()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout(widget)
        self.setCentralWidget(widget)
        
        file_path = "polygon.ply"
        self.pcd = o3d.io.read_point_cloud(file_path)

        self.vis = o3d.visualization.VisualizerWithEditing()
        self.vis.create_window()
        self.vis.add_geometry(self.pcd)

        hwnd = win32gui.FindWindowEx(0, 0, None, "Open3D - free view")
        self.window = QtGui.QWindow.fromWinId(hwnd)    

        self.windowcontainer = self.createWindowContainer(self.window, widget)
        layout.addWidget(self.windowcontainer, 0, 0)
        
        self.thread = QtCore.QThread()
        self.worker = Worker()
        self.thread.started.connect(lambda: self.worker.run(self.vis))
        self.thread.start()
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.blub)
        timer.start(100)
        #print("starting vis")

        btn = QtWidgets.QPushButton(text="test")
        btn.clicked.connect(lambda: print("Button pressed!"))
        layout.addWidget(btn)
    
    def blub(self):
        #Function to keep PySide eventloop running
        pass
    
    def start_vis(self):
        print("thread start")
        self.vis.run()
        print("thread end")

    def update_vis(self):
        #self.vis.update_geometry()
        self.vis.poll_events()
        self.vis.update_renderer()

    def closeEvent(self, event):
        self.vis.destroy_window()
        self.thread.quit()
        event.accept()

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.setWindowTitle('o3d Embed')
    form.setGeometry(100, 100, 600, 500)
    form.show()
    sys.exit(app.exec())