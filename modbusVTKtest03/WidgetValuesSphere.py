"""
   作者：zhan
   日期：2022年01月31日
"""
from PySide6 import QtWidgets, QtCore
from mvc.MyCtrl import MyView
from ui_WidgetValuesSphere import Ui_WidgetValuesSphere


class UiWidgetValuesSphere(QtWidgets.QWidget, Ui_WidgetValuesSphere, MyView):
    def __init__(self, parent=None):
        super(UiWidgetValuesSphere, self).__init__(parent)

        self.setupUi(self)

    def slot_a(self, **kwargs):  # 显示
        pos = kwargs["pos"]
        self.lineEdit_X.setText(str(pos[0]))
        self.lineEdit_Y.setText(str(pos[1]))
        self.lineEdit_Z.setText(str(pos[2]))

