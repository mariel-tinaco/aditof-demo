import sys, os
from PySide6 import QtWidgets, QtCore, QtGui



if __name__ == "__main__":

    from src.app_entry.app import TOFDemoApplication
    from src.views.widgets.samplewin import MyWindow

    app = TOFDemoApplication()

    window = MyWindow()
    window.show()

    sys.exit(app.exec())