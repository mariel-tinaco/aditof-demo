# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BaseToFView.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_BaseToFView(object):
    def setupUi(self, BaseToFView):
        if not BaseToFView.objectName():
            BaseToFView.setObjectName(u"BaseToFView")
        BaseToFView.resize(400, 300)
        self.verticalLayout = QVBoxLayout(BaseToFView)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerframe = QFrame(BaseToFView)
        self.headerframe.setObjectName(u"headerframe")
        self.headerframe.setFrameShape(QFrame.StyledPanel)
        self.headerframe.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.headerframe)

        self.subheaderframe = QFrame(BaseToFView)
        self.subheaderframe.setObjectName(u"subheaderframe")
        self.subheaderframe.setFrameShape(QFrame.StyledPanel)
        self.subheaderframe.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.subheaderframe)

        self.viewframe = QFrame(BaseToFView)
        self.viewframe.setObjectName(u"viewframe")
        self.viewframe.setFrameShape(QFrame.StyledPanel)
        self.viewframe.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.viewframe)


        self.retranslateUi(BaseToFView)

        QMetaObject.connectSlotsByName(BaseToFView)
    # setupUi

    def retranslateUi(self, BaseToFView):
        BaseToFView.setWindowTitle(QCoreApplication.translate("BaseToFView", u"Form", None))
    # retranslateUi

