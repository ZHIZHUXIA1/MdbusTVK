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
        self.dict = {"IP": "127.0.0.1", "PORT": "502", "Name": "PLC1", "Start": "0", "Num": "3", }
        self.dict1 = {"IP": "127.0.0.1", "PORT": "503", "Name": "PLC2", "Start": "0", "Num": "3", }
        self.pushButton.clicked.connect(self.showPos)
        self.ctrl = MyCtrl()
        self.widgetVTK.ren.set_mvc_control(self.ctrl)
        self.widgetValues.set_mvc_control(self.ctrl)
        self.iTActor = {"interActor": self.widgetVTK}

    def showPos(self):  # 显示位置
        appointPos = self.lineEdit.text()
        iTActor = {"interActor": self.widgetVTK}
        # threading2 = threading.Thread(target=self.ctrl.run, args=(self.iTActor,))
        # threading2.start()
        threading1 = threading.Thread(target=self.ctrl.StartReadModbusTcp, args=(self.dict,))
        threading1.start()
        threading2 = threading.Thread(target=self.ctrl.StartReadModbusTcp, args=(self.dict1,))
        threading2.start()
        threading3 = threading.Thread(target=self.ctrl.run, args=(iTActor,))
        threading3.start()
        #self.ctrl.run(iTActor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window1 = UiMainWindow()
    window1.show()
    # window1.iren.Initialize()  # Need this line to actually show the render inside Qt
    sys.exit(app.exec())
