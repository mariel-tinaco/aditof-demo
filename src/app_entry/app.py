import sys, os
import logging
from PySide6 import QtWidgets, QtCore, QtGui

from ..controllers.maincontroller import MainController
# from ..views.widgets.tofmainwindow import MainWindow
from ..views.widgets.styledmainview import MainWindow
from ..models.mainmodel import MainModel

class TOFDemoApplication (QtCore.QObject):

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__app = QtWidgets.QApplication (sys.argv)
        self.controller = MainController (MainWindow(), MainModel())

    def start (self):
        self.controller.start()
        self.controller.connect_signals()
    @property
    def app (self):
        return self.__app

    def exec(self):
        return self.__app.exec()

if __name__ == "__main__":
    sys.path.append(os.path.join(os.getcwd(), '..'))

    app = TOFDemoApplication()
    app.start()

    sys.exit(app.exec())