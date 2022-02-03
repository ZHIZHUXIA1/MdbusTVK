"""
   作者：zhan
   日期：2022年02月03日
"""
from PySide6 import QtWidgets
from mvc.MyCtrl import MyView
from ui_WidgetValuesSphere import Ui_WidgetValuesSphere
from ui_widgetvalue import ui_widgetvalue


class WidgetValues (QtWidgets.QWidget, ui_widgetvalue, MyView):
    def __init__(self, parent=None):
        super(WidgetValues, self).__init__(parent)
        self.setupUi(self)



