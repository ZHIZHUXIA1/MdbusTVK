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
bucket = "bucket1"
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
            time.sleep(1)
            try:
                master = ms.TcpMaster(dict["IP"], int(dict["PORT"]))
                master.set_timeout(5.0)
                self.dictReadTag = master.execute(1, de.READ_HOLDING_REGISTERS, int(dict["Start"]), int(dict["Num"]))
                p = influxdb_client.Point("mem").tag("location", dict["Name"])  .field("posx", self.dictReadTag[0]) \
                .field("posy", self.dictReadTag[1]).field("posz", self.dictReadTag[2])
                write_api.write(bucket=bucket, org=org, record=p)
            except Exception as e:
                print(dict["Name"], e)








def readEthernetIP(dict):
  source = proxy(dict["host"
                      ""])
  while True:
    time.sleep(1)
    try:
      val, = source.read(dict["tag_name"], dict["route_path"])
      val1, = source.read(dict["tag_name1"], dict["route_path"])
      val2, = source.read(dict["tag_name2"], dict["route_path"])
      p = influxdb_client.Point("mem").tag("location", dict["id"])\
        .field("dist", val[0] / 100.0).field("luff", val[1] / 100.0).field("slew", val[2] / 100.0).field("belt", val[4])\
        .field("flow_cur", val[15]).field("flow_set", val[20]).field("flow_accumulate", val[17]).field("accumulate_set", val[18])\
        .field("mode", val[19]).field("bucket_current", val[11]).field("flow1", val1[33]).field("angle_left", val2[0] / 100.0).field("angle_right", val2[1] / 100.0)

    except Exception as e:
      print("%s, read data error! message: %s" % (dict["id"], e))
      source = proxy(dict["host"], route_path=dict["route_path"])

