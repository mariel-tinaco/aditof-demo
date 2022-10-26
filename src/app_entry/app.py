import sys, os
from PySide6 import QtWidgets, QtCore, QtGui

class TOFDemoApplication (QtCore.QObject):

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__app = QtWidgets.QApplication (sys.argv)


    @property
    def app (self):
        return self.__app

    def exec(self):
        return self.__app.exec()

if __name__ == "__main__":
    sys.path.append(os.path.join(os.getcwd(), '..'))
    from views.widgets.samplewin import MyWindow

    app = TOFDemoApplication()

    window = MyWindow()
    window.show()

    sys.exit(app.exec())