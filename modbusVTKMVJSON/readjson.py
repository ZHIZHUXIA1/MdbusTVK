"""
   作者：zhan
   日期：2022年02月03日
"""
import json
import time


class readjson:
    SRNUM = 1

    def runnum():
        path = 'json.json'
        f = open(path, 'r', encoding='utf-8')
        m = json.load(f)
        list1 = m["SRdata"]
        SRNUM = len(list1)
        return SRNUM

    def __init__(self, namefrom):
        self.dict = {}
        self.Name = namefrom
        self.NUM = int(self.Name[2:])
        self.path = 'json.json'
        self.f = open(self.path, 'r', encoding='utf-8')
        self.m = json.load(self.f)
        self.dict = self.m["SRdata"][self.NUM - 1]


if __name__ == '__main__':
    while True:
        time.sleep(2)
        c0 = readjson.runnum()
        c1 = readjson("SR1")
        c2 = readjson("SR2")
        print(c1.dict)
        print(c2.dict["Name"])

