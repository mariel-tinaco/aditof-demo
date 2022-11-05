from PySide6 import QtWidgets, QtCore, QtGui

class BaseDemo (QtCore.QObject):

    def __init__ (self, mainview):
        self.mainview = mainview

