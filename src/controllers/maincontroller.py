from PySide6 import QtWidgets, QtCore, QtGui

from src.controllers.tofcontroller import ToFController

class MainController (QtCore.QObject):

    def __init__(self, view, model):
        super(MainController, self).__init__()

        self.view = view
        self.model = model
        self.tofctrl = ToFController()

    def connect_signals (self):
        self.view.signalRefresh.connect(self.refresh)
        

    @QtCore.Slot()
    def refresh (self):
        self.tofctrl.initialize()
        toflist = [cam.dev_id for cam in self.tofctrl.available_cameras]
        self.view.setCameraOptions(toflist)

    def start (self):
        self.view.show()