import random

from signalslot import Signal
from ControlBase import CtrlBase
from ViewBase import ViewBase
from ReadModbusTcp import ReadModbusTcp
import time
import threading
from readjson import readjson


class MyCtrl(CtrlBase, ReadModbusTcp):

    def __init__(self, name):
        self.name = name
        read1 = readjson(self.name)
        self.dict = read1.dict
        self.signal = Signal()
        threading1 = threading.Thread(target=self.StartReadModbusTcp, args=(self.dict,))
        threading1.start()

    def runWhileTure(self, kwargs):
        while True:
            if self.timeout == 0:
                iTActor = {"interActor": kwargs["interActor"]}
                position = self.dictReadTag
                pos = {"pos": position, }
                self.signal.emit(**pos, **iTActor)
                time.sleep(1)
            else:
                print("超时等待中")
                time.sleep(3)

    def run(self, kwargs):
        threadingRun = threading.Thread(target=self.runWhileTure, args=(kwargs,))
        threadingRun.start()


class MyView(ViewBase):
    def set_mvc_control(self, ctrl):
        super().set_mvc_control(ctrl)
        ctrl.signal.connect(self.slot_a)

    def slot_a(self, **kwargs):
        pass
