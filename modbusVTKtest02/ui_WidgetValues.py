# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WidgetValues.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_WidgetValues(object):
    def setupUi(self, WidgetValues):
        if not WidgetValues.objectName():
            WidgetValues.setObjectName(u"WidgetValues")
        WidgetValues.resize(818, 810)
        self.layoutWidget = QWidget(WidgetValues)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 131, 295))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.lineEdit_Z = QLineEdit(self.layoutWidget)
        self.lineEdit_Z.setObjectName(u"lineEdit_Z")

        self.gridLayout.addWidget(self.lineEdit_Z, 2, 2, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.lineEdit_Z_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_Z_2.setObjectName(u"lineEdit_Z_2")

        self.gridLayout.addWidget(self.lineEdit_Z_2, 5, 1, 1, 2)

        self.lineEdit_Y = QLineEdit(self.layoutWidget)
        self.lineEdit_Y.setObjectName(u"lineEdit_Y")

        self.gridLayout.addWidget(self.lineEdit_Y, 1, 2, 1, 1)

        self.lineEdit_X = QLineEdit(self.layoutWidget)
        self.lineEdit_X.setObjectName(u"lineEdit_X")

        self.gridLayout.addWidget(self.lineEdit_X, 0, 2, 1, 1)

        self.lineEdit_X_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_X_2.setObjectName(u"lineEdit_X_2")

        self.gridLayout.addWidget(self.lineEdit_X_2, 3, 1, 1, 2)

        self.lineEdit_Y_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_Y_2.setObjectName(u"lineEdit_Y_2")

        self.gridLayout.addWidget(self.lineEdit_Y_2, 4, 1, 1, 2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)


        self.retranslateUi(WidgetValues)

        QMetaObject.connectSlotsByName(WidgetValues)
    # setupUi

    def retranslateUi(self, WidgetValues):
        WidgetValues.setWindowTitle(QCoreApplication.translate("WidgetValues", u"Values", None))
        self.label_5.setText(QCoreApplication.translate("WidgetValues", u"Cone(X)", None))
        self.label.setText(QCoreApplication.translate("WidgetValues", u"Sphere(X):", None))
        self.label_2.setText(QCoreApplication.translate("WidgetValues", u"Sphere(Y)", None))
        self.label_6.setText(QCoreApplication.translate("WidgetValues", u"Cone(Y)", None))
        self.label_4.setText(QCoreApplication.translate("WidgetValues", u"Cone(Z)", None))
        self.label_3.setText(QCoreApplication.translate("WidgetValues", u"Sphere(Z)", None))
    # retranslateUi

