from typing import Iterable
from PySide6 import QtWidgets, QtCore, QtGui

from ..widgets.tofappwindow import BaseTofView, DNNView

class DemoListStack (QtCore.QObject):

    def __init__ (self, *items : Iterable[QtWidgets.QWidget]):
        super(DemoListStack, self).__init__()
        
        self._leftlist = QtWidgets.QListWidget()
        self._stackedwidget = QtWidgets.QStackedWidget()

        for i, Item in enumerate(items):
            item = Item (parent=self._stackedwidget)

            self._leftlist.insertItem(i, item.__displayname__)
            self._stackedwidget.addWidget(item)

        self._leftlist.currentRowChanged.connect (lambda x : self._stackedwidget.setCurrentIndex(x))

    def attach (self, listframe : QtWidgets.QFrame, stackframe : QtWidgets.QFrame):
        
        optionslayout = QtWidgets.QVBoxLayout()
        optionslayout.addWidget(self._leftlist)        
        listframe.setLayout(optionslayout)

        panelslayout = QtWidgets.QHBoxLayout()
        panelslayout.addWidget(self._stackedwidget)
        stackframe.setLayout(panelslayout)
        
    def addDemo (self, item):
        self._leftlist.addItem(item)
        self._stackedwidget.addWidget(item)


if __name__ == "__main__":

    liststack = DemoListStack (BaseTofView(), DNNView())
