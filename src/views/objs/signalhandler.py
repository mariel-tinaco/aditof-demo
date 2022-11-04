from PySide6 import QtCore, QtWidgets

class ViewSignalHandler (QtCore.QObject):

    def __init__ (self, view : QtWidgets.QWidget):
        super().__init__()
