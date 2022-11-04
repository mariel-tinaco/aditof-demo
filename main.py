import sys, os
from PySide6 import QtWidgets, QtCore, QtGui


def main():
    from src.app_entry.app import TOFDemoApplication
    app = TOFDemoApplication()
    app.start()
    sys.exit(app.exec())


if __name__ == "__main__":

    main()