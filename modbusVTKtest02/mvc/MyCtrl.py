import random

from signalslot import Signal
from ControlBase import CtrlBase
from ViewBase import ViewBase
from ReadModbusTcp import ReadModbusTcp
import time
import threading


class MyCtrl(CtrlBase, ReadModbusTcp):
    def __init__(self):
        self.signal = Signal()
        self.dict = {"IP": "127.0.0.1", "PORT": "502", "Name": "PLC1", "Start": "0", "Num": "3", }
        self.dict1 = {"IP": "127.0.0.1", "PORT": "503", "Name": "PLC2", "Start": "0", "Num": "3", }
        threading1 = threading.Thread(target=self.StartReadModbusTcp, args=(self.dict,))
        threading1.start()
        threading2 = threading.Thread(target=self.StartReadModbusTcp, args=(self.dict1,))
        threading2.start()

    def runWhileTure(self, kwargs):
        while True:
            iTActor = {"interActor": kwargs["interActor"]}
            positionPLC1 = self.dictReadTag["PLC1"]
            positionPLC2 = self.dictReadTag["PLC2"]
            pos = {"posPLC1": positionPLC1, "posPLC2": positionPLC2}
            self.signal.emit(**pos, **iTActor)
            time.sleep(1)

    def run(self, kwargs):
        threadingRun = threading.Thread(target=self.runWhileTure, args=(kwargs,))
        threadingRun.start()

    # def GetTcpTag(self):


class MyView(ViewBase):
    def set_mvc_control(self, ctrl):
        super().set_mvc_control(ctrl)
        ctrl.signal.connect(self.slot_a)

    def slot_a(self, **kwargs):
        pass
