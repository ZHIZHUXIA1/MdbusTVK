# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetValuesCone.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_WidgetValuesCone(object):
    def setupUi(self, WidgetValuesCone):
        if not WidgetValuesCone.objectName():
            WidgetValuesCone.setObjectName(u"WidgetValuesCone")
        WidgetValuesCone.resize(818, 810)
        self.layoutWidget = QWidget(WidgetValuesCone)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(6, 7, 111, 91))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_X_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_X_2.setObjectName(u"lineEdit_X_2")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_X_2)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_Y_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_Y_2.setObjectName(u"lineEdit_Y_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Y_2)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_Z_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_Z_2.setObjectName(u"lineEdit_Z_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_Z_2)


        self.retranslateUi(WidgetValuesCone)

        QMetaObject.connectSlotsByName(WidgetValuesCone)
    # setupUi

    def retranslateUi(self, WidgetValuesCone):
        WidgetValuesCone.setWindowTitle(QCoreApplication.translate("WidgetValuesCone", u"Values", None))
        self.label_4.setText(QCoreApplication.translate("WidgetValuesCone", u"Cone(X):", None))
        self.label_5.setText(QCoreApplication.translate("WidgetValuesCone", u"Cone(Y)", None))
        self.label_6.setText(QCoreApplication.translate("WidgetValuesCone", u"Cone(Z)", None))
    # retranslateUi

