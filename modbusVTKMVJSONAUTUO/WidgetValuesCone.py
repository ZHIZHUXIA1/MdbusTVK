"""
   作者：zhan
   日期：2022年01月31日
"""
from PySide6 import QtWidgets, QtCore
from mvc.MyCtrl import MyView
from ui_WidgetValuesCone import Ui_WidgetValuesCone


class UiWidgetValuesCone(QtWidgets.QWidget, Ui_WidgetValuesCone, MyView):
    def __init__(self, parent=None):
        super(UiWidgetValuesCone, self).__init__(parent)
        self.setupUi(self)

    def slot_a(self, **kwargs):
        pos = kwargs["pos"]
        self.lineEdit_X_2.setText(str(pos[0]))
        self.lineEdit_Y_2.setText(str(pos[1]))
        self.lineEdit_Z_2.setText(str(pos[2]))

