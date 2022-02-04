"""
   作者：zhan
   日期：2022年01月22日
"""
from __future__ import absolute_import, print_function, division

import time

import influxdb_client
import modbus_tk.defines as de
import modbus_tk.modbus_tcp as ms
from cpppo.server.enip.get_attribute import proxy
from influxdb_client.client.write_api import SYNCHRONOUS

url = "http://127.0.0.1:8086"
token = "ciayJb8Fofs8g9rUaDVXRQLjHf8D9cNdtOxG3_BRPH93Km7w-bxv8tFLXyVK56Bp6qQdLU5kz2iy2L4AyEIpRw=="
org = "Z"
bucket = "bucket2"
client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)


class ReadModbusTcp:
    dictReadTag = []

    def __init__(self):
        pass

    def StartReadModbusTcp(self, dict):
        while True:

            try:
                master = ms.TcpMaster(dict["IP"], int(dict["PORT"]))
                master.set_timeout(1.0)
                self.dictReadTag = master.execute(1, de.READ_HOLDING_REGISTERS, int(dict["Start"]), int(dict["Num"]))
                self.timeout = 0
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
