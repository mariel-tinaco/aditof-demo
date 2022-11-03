# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BaseMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topframe = QFrame(self.centralwidget)
        self.topframe.setObjectName(u"topframe")
        self.topframe.setStyleSheet(u"background-color:gray")
        self.topframe.setFrameShape(QFrame.StyledPanel)
        self.topframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topframe)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logoframe = QFrame(self.topframe)
        self.logoframe.setObjectName(u"logoframe")
        self.logoframe.setStyleSheet(u"background-color:blue")
        self.logoframe.setFrameShape(QFrame.StyledPanel)
        self.logoframe.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.logoframe)

        self.buttonsframe = QFrame(self.topframe)
        self.buttonsframe.setObjectName(u"buttonsframe")
        self.buttonsframe.setStyleSheet(u"background-color:darkgray")
        self.buttonsframe.setFrameShape(QFrame.StyledPanel)
        self.buttonsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.buttonsframe)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnslayout = QHBoxLayout()
        self.btnslayout.setObjectName(u"btnslayout")

        self.verticalLayout_2.addLayout(self.btnslayout)


        self.horizontalLayout_2.addWidget(self.buttonsframe)

        self.utilsframe = QFrame(self.topframe)
        self.utilsframe.setObjectName(u"utilsframe")
        self.utilsframe.setStyleSheet(u"b")
        self.utilsframe.setFrameShape(QFrame.StyledPanel)
        self.utilsframe.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.utilsframe)


        self.verticalLayout.addWidget(self.topframe)

        self.middleframe = QFrame(self.centralwidget)
        self.middleframe.setObjectName(u"middleframe")
        self.middleframe.setStyleSheet(u"QFrame{background-color: black}")
        self.middleframe.setFrameShape(QFrame.StyledPanel)
        self.middleframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.middleframe)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.optionsframe = QFrame(self.middleframe)
        self.optionsframe.setObjectName(u"optionsframe")
        self.optionsframe.setStyleSheet(u"background-color:gray")
        self.optionsframe.setFrameShape(QFrame.StyledPanel)
        self.optionsframe.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.optionsframe)

        self.panelsframe = QFrame(self.middleframe)
        self.panelsframe.setObjectName(u"panelsframe")
        self.panelsframe.setFrameShape(QFrame.StyledPanel)
        self.panelsframe.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.panelsframe)


        self.verticalLayout.addWidget(self.middleframe)

        self.bottomframe = QFrame(self.centralwidget)
        self.bottomframe.setObjectName(u"bottomframe")
        self.bottomframe.setStyleSheet(u"background: gray")
        self.bottomframe.setFrameShape(QFrame.StyledPanel)
        self.bottomframe.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.bottomframe)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

