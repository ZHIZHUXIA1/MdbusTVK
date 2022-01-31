"""
   作者：zhan
   日期：2022年01月22日
"""
import modbus_tk.modbus_tcp as ms
import modbus_tk.defines as de
import time
import threading


# modbustcp master
class ReadModbusTcp:
    dictReadTag =[]

    def __init__(self):
        pass

    def StartReadModbusTcp(self, dict):
        while True:
            time.sleep(0.3)
            try:
                master = ms.TcpMaster(dict["IP"], int(dict["PORT"]))
                master.set_timeout(5.0)
                self.dictReadTag = master.execute(1, de.READ_HOLDING_REGISTERS, int(dict["Start"]), int(dict["Num"]))

            except Exception as e:
                print(dict["Name"], e)


if __name__ == '__main__':

    dict1 = {"IP": "127.0.0.1", "PORT": "502", "Name": "PLC1", "Start": "0", "Num": "3", }
    dict2 = {"IP": "127.0.0.1", "PORT": "503", "Name": "PLC2", "Start": "0", "Num": "3", }

    READPLC1 = ReadModbusTcp()
    READPLC2 = ReadModbusTcp()
    threading1 = threading.Thread(target=READPLC1.StartReadModbusTcp, args=(dict1,))
    threading2 = threading.Thread(target=READPLC2.StartReadModbusTcp, args=(dict2,))
    threading1.start()
    threading2.start()
    while True:
        time.sleep(1)
        list1 = READPLC1.dictReadTag["PLC1"]
        list2 = READPLC2.dictReadTag["PLC2"]
        print(list1)
        print(list2)
        time.sleep(1)
    # print(READPLC2.dictreadtag)
