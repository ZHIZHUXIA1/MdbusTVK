# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QToolBar, QVBoxLayout, QWidget)

from WidgetVTK import WidgetVTK

class Ui_WindowBase(object):
    def setupUi(self, WindowBase):
        if not WindowBase.objectName():
            WindowBase.setObjectName(u"WindowBase")
        WindowBase.resize(800, 659)
        self.centralwidget = QWidget(WindowBase)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widgetVTK = QWidget(self.centralwidget)
        self.widgetVTK.setObjectName(u"widgetVTK")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetVTK.sizePolicy().hasHeightForWidth())
        self.widgetVTK.setSizePolicy(sizePolicy)
        self.widgetvtk = WidgetVTK(self.widgetVTK)
        self.widgetvtk.setObjectName(u"widgetvtk")
        self.widgetvtk.setGeometry(QRect(179, 20, 581, 511))

        self.horizontalLayout_2.addWidget(self.widgetVTK)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        WindowBase.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(WindowBase)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        WindowBase.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(WindowBase)
        self.statusbar.setObjectName(u"statusbar")
        WindowBase.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(WindowBase)
        self.toolBar.setObjectName(u"toolBar")
        WindowBase.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(WindowBase)

        QMetaObject.connectSlotsByName(WindowBase)
    # setupUi

    def retranslateUi(self, WindowBase):
        WindowBase.setWindowTitle(QCoreApplication.translate("WindowBase", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("WindowBase", u"PushButton", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("WindowBase", u"toolBar", None))
    # retranslateUi

