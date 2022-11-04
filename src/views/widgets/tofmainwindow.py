import sys, os
from PySide6 import QtWidgets, QtCore, QtGui

from src.views.objs.liststack import DemoListStack
from src.views.widgets.tofappwindow import BaseTofView, DNNView

from ..resources.widgets.Ui_BaseMainWindow import Ui_MainWindow

class MainWindow (QtWidgets.QMainWindow, Ui_MainWindow):

    signalRefresh = QtCore.Signal()

    def __init__(self):
        super(MainWindow, self).__init__()
        '''Load the ui'''
        self.setupUi(self)

        # Adjusts initial screen to the resolution of the primary screen display
        screen_width = self.screen().size().width()
        screen_height = self.screen().size().height()
        self.resize (screen_width, screen_height)
        topframeheight = int(self.height()/10)
        self.topframe.setFixedHeight(topframeheight)
        self.bottomframe.setFixedHeight(int(self.height()/15))
        
        leftpanelwidth = int(self.width()/7)
        rightpanelwidth = int(self.width()/7)
        self.optionsframe.setFixedWidth(leftpanelwidth)
        self.logoframe.setFixedWidth(leftpanelwidth)
        self.utilsframe.setFixedWidth(rightpanelwidth)

        self.cameracombobox = QtWidgets.QComboBox()
        self.refreshbutton = QtWidgets.QPushButton("Refresh")
        self.configbutton = QtWidgets.QPushButton("Configure")
        self.toggleplaybutton = QtWidgets.QPushButton("Play")
        self.snapshotbutton = QtWidgets.QPushButton ("Capture")

        btnside = topframeheight

        self.cameracombobox.setFixedSize(int(self.width()/8), btnside)
        self.refreshbutton.setFixedSize(btnside, btnside)
        self.configbutton.setFixedSize(btnside, btnside)
        self.toggleplaybutton.setFixedSize(btnside, btnside)
        self.snapshotbutton.setFixedSize(btnside, btnside)

        self.btnslayout.addWidget(self.cameracombobox)
        self.btnslayout.addWidget(self.refreshbutton)
        self.btnslayout.addWidget(self.configbutton)
        self.btnslayout.addWidget(self.toggleplaybutton)
        self.btnslayout.addWidget(self.snapshotbutton)
        self.btnslayout.addStretch(-1)

        # Toggle button config
        self.toggleplaybutton.setCheckable(True)
        self.toggleplaybutton.clicked.connect(self.playpause_toggle)

        # List widgets and Stacked widgets config
        self.demo_widgets = DemoListStack(BaseTofView, DNNView)
        self.demo_widgets.attach (self.optionsframe, self.panelsframe)

        # Refresh button config
        self.refreshbutton.setCheckable(True)
        self.refreshbutton.clicked.connect(lambda : self.signalRefresh.emit())

    def playpause_toggle (self):
        if self.toggleplaybutton.isChecked():
            self.toggleplaybutton.setText("Pause")
        else:
            self.toggleplaybutton.setText("Play")

    def setCameraOptions (self, camoptions):
        self.cameracombobox.addItems(camoptions)


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