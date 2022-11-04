from PySide6 import QtWidgets, QtGui, QtCore


class CustomToggleButton (QtWidgets.QPushButton):

    def __init__ (self):
        super(CustomToggleButton, self).__init__ ()

        self.setCheckable(True)

