import sys, os
from PySide6 import QtWidgets, QtCore, QtGui

from ..resources.widgets.Ui_BaseToFView import Ui_BaseToFView

class BaseTofView (QtWidgets.QWidget, Ui_BaseToFView):

    __displayname__ = "Base Camera View"

    def __init__ (self, *args, **kwargs):
        super(BaseTofView, self).__init__ (*args, **kwargs)
        
        self.view_label = QtWidgets.QLabel(self)
        self.setup()

    def setup (self):
        self.setupUi(self)
        self.headerframe.setFixedHeight(int(self.parent().height()/10))
        self.headerframe.setStyleSheet("background-color:green")

        self.subheaderframe.setFixedHeight(int(self.parent().height()/10))
        self.subheaderframe.setStyleSheet("background-color:yellow")

        viewlayout = QtWidgets.QHBoxLayout()
        viewlayout.addWidget(self.view_label)

        self.viewframe.setLayout(viewlayout)

    @QtCore.Slot(QtGui.QImage)
    def setImage (self, image):
        self.view_label.setPixmap(QtGui.QPixmap.fromImage(image))

class DNNView (QtWidgets.QWidget):

    __displayname__ = "DNN View"

    def __init__ (self, *args, **kwargs):
        super(DNNView, self).__init__ (*args, **kwargs)

        self.setup()

    def setup (self):
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel(self.__displayname__)
        label.setStyleSheet(
            """
            color: white
            """
        )
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    view = BaseTofView()
    view.show()

    sys.exit(app.exec())
