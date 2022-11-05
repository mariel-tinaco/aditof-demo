# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StyledMainView.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(970, 600)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:#fff;\n"
"}\n"
"#centralwidget{\n"
"	background-image: url(:/resources/assets/6173960.jpg);\n"
"}\n"
"\n"
"#topframe{\n"
"	background-color: rgba(0, 0, 0,150);\n"
"}\n"
"\n"
"#optionsframe{\n"
"	background-color: rgba(0, 0, 0,150);\n"
"}\n"
"\n"
"#statusframe{\n"
"	background-color: rgb(0, 120, 215)\n"
"}\n"
"\n"
"#irframe{\n"
"	background-color: rgba(30, 30, 30,150);\n"
"}\n"
"\n"
"#depthframe{\n"
"	background-color: rgba(30, 30, 30,150);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainlayout = QVBoxLayout(self.centralwidget)
        self.mainlayout.setSpacing(0)
        self.mainlayout.setObjectName(u"mainlayout")
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.topframe = QFrame(self.centralwidget)
        self.topframe.setObjectName(u"topframe")
        self.topframe.setMinimumSize(QSize(0, 30))
        self.topframe.setFrameShape(QFrame.StyledPanel)
        self.topframe.setFrameShadow(QFrame.Raised)
        self.topframelayout = QHBoxLayout(self.topframe)
        self.topframelayout.setSpacing(0)
        self.topframelayout.setObjectName(u"topframelayout")
        self.topframelayout.setContentsMargins(0, 0, 0, 0)
        self.logoframe = QFrame(self.topframe)
        self.logoframe.setObjectName(u"logoframe")
        self.logoframe.setMinimumSize(QSize(200, 0))
        self.logoframe.setFrameShape(QFrame.StyledPanel)
        self.logoframe.setFrameShadow(QFrame.Raised)

        self.topframelayout.addWidget(self.logoframe)

        self.controlsframe = QFrame(self.topframe)
        self.controlsframe.setObjectName(u"controlsframe")
        self.controlsframe.setFrameShape(QFrame.StyledPanel)
        self.controlsframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.controlsframe)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cameracombobox = QComboBox(self.controlsframe)
        self.cameracombobox.addItem("")
        self.cameracombobox.setObjectName(u"cameracombobox")
        self.cameracombobox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.cameracombobox)

        self.refreshbutton = QPushButton(self.controlsframe)
        self.refreshbutton.setObjectName(u"refreshbutton")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshbutton.sizePolicy().hasHeightForWidth())
        self.refreshbutton.setSizePolicy(sizePolicy)
        self.refreshbutton.setStyleSheet(u"*{\n"
"	padding:10px\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  border: 1px solid red;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/resources/assets/icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshbutton.setIcon(icon)
        self.refreshbutton.setFlat(True)

        self.horizontalLayout.addWidget(self.refreshbutton)

        self.configbutton = QPushButton(self.controlsframe)
        self.configbutton.setObjectName(u"configbutton")
        self.configbutton.setStyleSheet(u"*{\n"
"	padding: 10px;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  border: 1px solid red;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/resources/assets/icons/configure.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.configbutton.setIcon(icon1)
        self.configbutton.setFlat(True)

        self.horizontalLayout.addWidget(self.configbutton)

        self.toggleplaybutton = QPushButton(self.controlsframe)
        self.toggleplaybutton.setObjectName(u"toggleplaybutton")
        self.toggleplaybutton.setStyleSheet(u"*{\n"
"	padding:10px;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  border: 1px solid red;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/resources/assets/icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleplaybutton.setIcon(icon2)
        self.toggleplaybutton.setFlat(True)

        self.horizontalLayout.addWidget(self.toggleplaybutton)

        self.snapshotbutton = QPushButton(self.controlsframe)
        self.snapshotbutton.setObjectName(u"snapshotbutton")
        self.snapshotbutton.setStyleSheet(u"*{\n"
"	padding:10px;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  border: 1px solid red;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/resources/assets/icons/capture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.snapshotbutton.setIcon(icon3)
        self.snapshotbutton.setFlat(True)

        self.horizontalLayout.addWidget(self.snapshotbutton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.topframelayout.addWidget(self.controlsframe)

        self.utilsframe = QFrame(self.topframe)
        self.utilsframe.setObjectName(u"utilsframe")
        self.utilsframe.setFrameShape(QFrame.StyledPanel)
        self.utilsframe.setFrameShadow(QFrame.Raised)

        self.topframelayout.addWidget(self.utilsframe)


        self.mainlayout.addWidget(self.topframe)

        self.midframe = QFrame(self.centralwidget)
        self.midframe.setObjectName(u"midframe")
        self.midframe.setFrameShape(QFrame.StyledPanel)
        self.midframe.setFrameShadow(QFrame.Raised)
        self.midframeLayout = QHBoxLayout(self.midframe)
        self.midframeLayout.setSpacing(0)
        self.midframeLayout.setObjectName(u"midframeLayout")
        self.midframeLayout.setContentsMargins(0, 0, 0, 0)
        self.optionsframe = QFrame(self.midframe)
        self.optionsframe.setObjectName(u"optionsframe")
        self.optionsframe.setMinimumSize(QSize(200, 0))
        self.optionsframe.setFrameShape(QFrame.StyledPanel)
        self.optionsframe.setFrameShadow(QFrame.Raised)
        self.listWidget = QListWidget(self.optionsframe)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(5, 1, 191, 201))
        self.listWidget.setMinimumSize(QSize(100, 0))

        self.midframeLayout.addWidget(self.optionsframe)

        self.panelsframe = QFrame(self.midframe)
        self.panelsframe.setObjectName(u"panelsframe")
        self.panelsframe.setFrameShape(QFrame.StyledPanel)
        self.panelsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.panelsframe)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.panelsframe)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.basedisplaypage = QWidget()
        self.basedisplaypage.setObjectName(u"basedisplaypage")
        self.verticalLayout_2 = QVBoxLayout(self.basedisplaypage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.basesettingsframe = QFrame(self.basedisplaypage)
        self.basesettingsframe.setObjectName(u"basesettingsframe")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.basesettingsframe.sizePolicy().hasHeightForWidth())
        self.basesettingsframe.setSizePolicy(sizePolicy1)
        self.basesettingsframe.setMinimumSize(QSize(0, 70))
        self.basesettingsframe.setFrameShape(QFrame.StyledPanel)
        self.basesettingsframe.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.basesettingsframe)

        self.basedisplayframe = QFrame(self.basedisplaypage)
        self.basedisplayframe.setObjectName(u"basedisplayframe")
        self.basedisplayframe.setFrameShape(QFrame.StyledPanel)
        self.basedisplayframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.basedisplayframe)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.irframe = QFrame(self.basedisplayframe)
        self.irframe.setObjectName(u"irframe")
        self.irframe.setFrameShape(QFrame.StyledPanel)
        self.irframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.irframe)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.irpixmaplabel = QLabel(self.irframe)
        self.irpixmaplabel.setObjectName(u"irpixmaplabel")

        self.verticalLayout_3.addWidget(self.irpixmaplabel)


        self.horizontalLayout_2.addWidget(self.irframe)

        self.depthframe = QFrame(self.basedisplayframe)
        self.depthframe.setObjectName(u"depthframe")
        self.depthframe.setFrameShape(QFrame.StyledPanel)
        self.depthframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.depthframe)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.depthpixmaplabel = QLabel(self.depthframe)
        self.depthpixmaplabel.setObjectName(u"depthpixmaplabel")

        self.verticalLayout_4.addWidget(self.depthpixmaplabel)


        self.horizontalLayout_2.addWidget(self.depthframe)


        self.verticalLayout_2.addWidget(self.basedisplayframe)

        self.stackedWidget.addWidget(self.basedisplaypage)
        self.dnnpage = QWidget()
        self.dnnpage.setObjectName(u"dnnpage")
        self.stackedWidget.addWidget(self.dnnpage)
        self.pointcloudpage = QWidget()
        self.pointcloudpage.setObjectName(u"pointcloudpage")
        self.stackedWidget.addWidget(self.pointcloudpage)
        self.bodytrackingpage = QWidget()
        self.bodytrackingpage.setObjectName(u"bodytrackingpage")
        self.stackedWidget.addWidget(self.bodytrackingpage)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.midframeLayout.addWidget(self.panelsframe)


        self.mainlayout.addWidget(self.midframe)

        self.statusframe = QFrame(self.centralwidget)
        self.statusframe.setObjectName(u"statusframe")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.statusframe.sizePolicy().hasHeightForWidth())
        self.statusframe.setSizePolicy(sizePolicy2)
        self.statusframe.setMinimumSize(QSize(0, 20))
        self.statusframe.setFrameShape(QFrame.StyledPanel)
        self.statusframe.setFrameShadow(QFrame.Raised)

        self.mainlayout.addWidget(self.statusframe)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cameracombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"(No Active Device)", None))

        self.refreshbutton.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
#if QT_CONFIG(shortcut)
        self.refreshbutton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.configbutton.setText(QCoreApplication.translate("MainWindow", u"CONFIGURE", None))
        self.toggleplaybutton.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.snapshotbutton.setText(QCoreApplication.translate("MainWindow", u"CAPTURE", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"BASE DISPLAY", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"DNN", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"POINT CLOUD", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"BODY TRACKING", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.irpixmaplabel.setText("")
        self.depthpixmaplabel.setText("")
    # retranslateUi

