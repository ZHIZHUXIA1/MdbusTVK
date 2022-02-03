# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetvalue.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

from WidgetValuesSphere import UiWidgetValuesSphere
from readjson import readjson


class ui_widgetvalue(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 120, 281))
        self.srnum = readjson.runnum()
        self.widgetlist = []
        for i in range(self.srnum):
            self.widgetlist.append(UiWidgetValuesSphere(self.widget))
            self.widgetlist[i].setObjectName(u"widgetsphere")
            self.viewpos = 20 + 80 * i
            self.widgetlist[i].setGeometry(QRect(1, self.viewpos, 120, 161))
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi
