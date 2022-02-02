import sys
from PySide6 import QtWidgets, QtCore
from mvc.MyCtrl import MyCtrl
from ui_MainWindow import Ui_MainWindow
import readxml


class UiMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(UiMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.ctrl1 = MyCtrl("SR1")
        self.ctrl2 = MyCtrl("SR2")
        self.pushButton.clicked.connect(self.showPos)
        self.widgetsphere.set_mvc_control(self.ctrl1)
        self.widgetcone.set_mvc_control(self.ctrl2)
        self.widgetvtk.actor.set_mvc_control(self.ctrl1)
        self.widgetvtk.actor1.set_mvc_control(self.ctrl2)

    def showPos(self):
        appointPos = self.lineEdit.text()
        iTActor = {"interActor": self.widgetvtk}
        self.ctrl1.run(iTActor)
        self.ctrl2.run(iTActor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window1 = UiMainWindow()
    window1.show()
    sys.exit(app.exec())
