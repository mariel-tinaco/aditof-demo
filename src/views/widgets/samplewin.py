from PySide6 import QtWidgets, QtCore, QtGui


class MyWindow (QtWidgets.QWidget):

    def __init__ (self, *args, **kwargs):
        super().__init__ (*args, **kwargs)

        layout = QtWidgets.QVBoxLayout()
        pb1 = QtWidgets.QPushButton("CLICK ME")

        layout.addWidget(pb1)
        self.setLayout(layout)