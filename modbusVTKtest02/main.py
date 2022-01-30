import random
import sys
from PySide6 import QtWidgets, QtCore
from mvc.MyCtrl import MyCtrl
from ui_MainWindow import Ui_MainWindow
import threading
import time


class UiMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(UiMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showPos)
        self.ctrl = MyCtrl()
        self.widgetVTK.ren.set_mvc_control(self.ctrl)
        self.widgetValues.set_mvc_control(self.ctrl)
        self.iTActor = {"interActor": self.widgetVTK}

    def showPos(self):
        appointPos = self.lineEdit.text()
        iTActor = {"interActor": self.widgetVTK}
        self.ctrl.run(iTActor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window1 = UiMainWindow()
    window1.show()
    # window1.iren.Initialize()  # Need this line to actually show the render inside Qt
    sys.exit(app.exec())
