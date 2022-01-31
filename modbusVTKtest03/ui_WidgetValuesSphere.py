# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetValuesSphere.ui'
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

class Ui_WidgetValuesSphere(object):
    def setupUi(self, WidgetValuesSphere):
        if not WidgetValuesSphere.objectName():
            WidgetValuesSphere.setObjectName(u"WidgetValuesSphere")
        WidgetValuesSphere.resize(818, 810)
        self.layoutWidget = QWidget(WidgetValuesSphere)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 111, 81))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_X = QLineEdit(self.layoutWidget)
        self.lineEdit_X.setObjectName(u"lineEdit_X")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_X)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_Y = QLineEdit(self.layoutWidget)
        self.lineEdit_Y.setObjectName(u"lineEdit_Y")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Y)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_Z = QLineEdit(self.layoutWidget)
        self.lineEdit_Z.setObjectName(u"lineEdit_Z")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_Z)


        self.retranslateUi(WidgetValuesSphere)

        QMetaObject.connectSlotsByName(WidgetValuesSphere)
    # setupUi

    def retranslateUi(self, WidgetValuesSphere):
        WidgetValuesSphere.setWindowTitle(QCoreApplication.translate("WidgetValuesSphere", u"Values", None))
        self.label.setText(QCoreApplication.translate("WidgetValuesSphere", u"Sphere(X):", None))
        self.label_2.setText(QCoreApplication.translate("WidgetValuesSphere", u"Sphere(Y)", None))
        self.label_3.setText(QCoreApplication.translate("WidgetValuesSphere", u"Sphere(Z)", None))
    # retranslateUi

