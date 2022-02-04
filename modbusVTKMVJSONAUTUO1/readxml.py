"""
   作者：zhan
   日期：2022年02月02日
"""
import xml.dom.minidom
import time


class readxml:
    SRNUM = 1

    def runnum():
        dom = xml.dom.minidom.parse('config.xml')
        root = dom.documentElement
        itemlist = root.getElementsByTagName('SR')
        SRNUM = len(itemlist)
        return SRNUM

    def runinfluxdb():
        dom = xml.dom.minidom.parse('config.xml')
        root = dom.documentElement
        influxdb1 = root.getElementsByTagName('InfluxDB')
        dict["Name"] = influxdb1.getAttribute("Name")
        dict["IP"] = influxdb1.getAttribute("IP")
        dict["PORT"] = influxdb1.getAttribute("PORT")
        dict["Start"] = influxdb1.item.getAttribute("Start")
        dict["Num"] = influxdb1.item.getAttribute("Num")
        return dict

    def __init__(self, namefrom):
        self.Name = namefrom
        self.dict = {}
        self.dom = xml.dom.minidom.parse('config.xml')
        self.root = self.dom.documentElement
        self.itemlist = self.root.getElementsByTagName('SR')
        self.NUM = int(self.Name[2:])
        self.item = self.itemlist[(self.NUM - 1)]
        self.dict["Name"] = self.item.getAttribute("Name")
        self.dict["IP"] = self.item.getAttribute("IP")
        self.dict["PORT"] = self.item.getAttribute("PORT")
        self.dict["Start"] = self.item.getAttribute("Start")
        self.dict["Num"] = self.item.getAttribute("Num")
        # self.dict1 = {"IP": "127.0.0.1", "PORT": "502", "Name": "PLC1", "Start": "0", "Num": "3", }


if __name__ == '__main__':
    while True:
        c0 = readxml.runnum()
        c1 = readxml("SR1")
        c2V = readxml("SR2")
        print(c1.dict)
        print(c1.dict)
        print(c0)
        time.sleep(1)
