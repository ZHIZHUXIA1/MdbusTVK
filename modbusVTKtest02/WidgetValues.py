import os
import random
import sys
# sys.path.append(os.path.abspath("./mvc"))
# from MyCtrl import *
from PySide6 import QtWidgets, QtCore
from mvc.MyCtrl import MyView
from ui_WidgetValues import Ui_WidgetValues


class UiWidgetValues(QtWidgets.QWidget, Ui_WidgetValues, MyView):
    def __init__(self, parent=None):
        super(UiWidgetValues, self).__init__(parent)
        self.setupUi(self)

    def slot_a(self, **kwargs):  # 显示
        pos = kwargs["posPLC1"]
        pos1 = kwargs["posPLC2"]
        self.lineEdit_X.setText(str(pos[0]))
        self.lineEdit_Y.setText(str(pos[1]))
        self.lineEdit_Z.setText(str(pos[2]))

        self.lineEdit_X_2.setText(str(pos1[0]))
        self.lineEdit_Y_2.setText(str(pos1[1]))
        self.lineEdit_Z_2.setText(str(pos1[2]))
