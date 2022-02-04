from PySide6 import QtWidgets
from PySide6.QtCore import QRect
from WidgetValuesSphere import UiWidgetValuesSphere
from readxml import readxml
from readjson import readjson
from ui_MainWindow import Ui_WindowBase


class UiMainWindow(QtWidgets.QMainWindow, Ui_WindowBase):
    def __init__(self, parent=None):
        super(UiMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.widgetlist = []
        self.autowidget()

    def autowidget(self):
        self.srnum = readjson.runnum()
        for i in range(self.srnum):
            self.widgetlist.append(UiWidgetValuesSphere(self.widgetVTK))
            self.widgetlist[i].setObjectName(u"widgetsphere")
            self.viewpos = 20 + 100 * i
            self.widgetlist[i].setGeometry(QRect(10, self.viewpos, 120, 161))
