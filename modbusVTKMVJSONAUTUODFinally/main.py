import sys
from PySide6 import QtWidgets, QtCore

from MainWindow import UiMainWindow
from mvc.MyCtrl import MyCtrl
from readxml import readxml
from readjson import readjson


class MainWindow(UiMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.srnum = readjson.runnum()
        self.ctrl = []
        for i in range(self.srnum):
            self.ctrl.append(MyCtrl("SR{}".format(i + 1)))
            self.widgetlist[i].set_mvc_control(self.ctrl[i])
            self.widgetvtk.action[i].set_mvc_control(self.ctrl[i])
        self.pushButton.clicked.connect(self.showPos)

    def showPos(self):
        appointPos = self.lineEdit.text()
        iTActor = {"interActor": self.widgetvtk}
        for i in range(self.srnum):
            self.ctrl[i].run(iTActor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window1 = MainWindow()
    window1.show()
    sys.exit(app.exec())
