import sys, os
from PySide6 import QtWidgets, QtCore, QtGui

from src.views.objs.liststack import DemoListStack
from src.views.widgets.tofappwindow import BaseTofView, DNNView

from ..resources.widgets.Ui_StyledMainView import Ui_MainWindow

class MainWindow (QtWidgets.QMainWindow, Ui_MainWindow):

    signalRefresh = QtCore.Signal()
    signalConfigure = QtCore.Signal()
    signalPlay = QtCore.Signal()
    signalPause = QtCore.Signal()

    def __init__ (self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.closeButton = QtWidgets.QPushButton(' ✕ ')
        self.closeButton.setEnabled(True)


        self.setupUi()
        self.__connect_signals()

    def connect_buttons (self):
        self.closeButton.clicked.connect(lambda : print("X"))

    def adjustToScreen (self):
        # Adjusts initial screen to the resolution of the primary screen display
        screen_width = self.screen().size().width()
        screen_height = self.screen().size().height()
        self.resize (screen_width, screen_height)

        topframeheight = int(self.height()/8)
        self.topframe.setFixedHeight(topframeheight)
        self.statusframe.setFixedHeight(int(self.height()/20))
        
        leftpanelwidth = int(self.width()/7)
        rightpanelwidth = int(self.width()/7)
        self.optionsframe.setFixedWidth(leftpanelwidth)

        self.logoframe.setFixedWidth(leftpanelwidth)
        self.utilsframe.setFixedWidth(rightpanelwidth)


    def __connect_signals (self):
        self.refreshbutton.clicked.connect(lambda : self.signalRefresh.emit())
        self.configbutton.clicked.connect(lambda : self.signalConfigure.emit())
        self.toggleplaybutton.clicked.connect(self.toggleStream)


    def toggleStream (self):
        if self.toggleplaybutton.isChecked():
            self.toggleplaybutton.setText('PAUSE')
            self.signalPlay.emit()
        else:
            self.toggleplaybutton.setText('PLAY')
            self.signalPause.emit()

    def setupUi(self):
        super().setupUi(self)
        self.adjustToScreen()
        self.toggleplaybutton.setCheckable(True)


    def setCameraOptions(self, camoptions):
        self.cameracombobox.clear()
        self.cameracombobox.addItems(camoptions)

    def setupStateMachine (self):
        ...

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # screen = QtWidgets.QApplication.primaryScreen()
    # screensize = screen.size()

    # print('Size: %d x %d' % (screensize.width(), screensize.height()))
    # rect = screen.availableGeometry()
    # print('Available: %d x %d' % (rect.width(), rect.height()))

    sys.exit(app.exec())