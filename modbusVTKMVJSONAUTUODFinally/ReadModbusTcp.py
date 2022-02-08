"""
   作者：zhan
   日期：2022年01月22日
"""
from __future__ import absolute_import, print_function, division

import time

import influxdb_client
import modbus_tk.defines as de
import modbus_tk.modbus_tcp as ms

from dataconversion import int_to_bit
from readjson import readjson
from influxdb_client.client.write_api import SYNCHRONOUS
import threading

influxdb = readjson.runinfluxdb()
url = influxdb["url"]
token = influxdb["token"]
org = influxdb["org"]
bucket = influxdb["bucket"]
client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)


class ReadModbusTcp:


    def __init__(self):
        pass

    def StartReadModbusTcp(self, dict, ):

        self.dictReadTag = []
        self.dictReadTag1 = []
        while True:

            try:

                master = ms.TcpMaster(dict["IP"], int(dict["PORT"]))
                master.set_timeout(1.0)
                self.dictReadTag1 = master.execute(1, de.READ_HOLDING_REGISTERS, int(dict["Start"]), int(dict["Num"]))
                self.timeout = 0
                self.inttobi = dict["Name"] + "bit"
                self.inttobi = int_to_bit()

                if len(self.dictReadTag) < (int(dict["Num"]) // 2):

                    for i in range(0, int(dict["Num"]), 2):
                        self.dictReadTag.append(self.inttobi.int_to_bit(self.dictReadTag1[i], self.dictReadTag1[i + 1]))

                else:

                    for i in range(0, int(dict["Num"]), 2):
                        i1 = i // 2
                        self.dictReadTag[i1] = self.inttobi.int_to_bit(self.dictReadTag1[i], self.dictReadTag1[i + 1])

            except Exception as e:
                self.timeout = 1
                print(dict["Name"], "读取数据出错", e)
                print(dict["Name"], "self.timeout=", self.timeout)

            try:

                p = influxdb_client.Point("mem").tag("location", dict["Name"]).field("posx", self.dictReadTag[0]) \
                    .field("posy", self.dictReadTag[1]).field("posz", self.dictReadTag[2])
                write_api.write(bucket=bucket, org=org, record=p)
            except Exception as s:
                print(dict["Name"], "写入数据库出错", s)
            time.sleep(1)

