"""
   作者：zhan
   日期：2022年02月04日
"""


class int_to_bit:

    def int_to_bit(self, intdata1, intdata2):
        self.upperint = intdata2 << 16
        self.lowerint = intdata1
        self.intall = self.upperint + self.lowerint
        self.binall = bin(self.intall).replace("0b", "")
        self.intc = int("10000000000000000000000000000000", 2)
        self.intall5 = ""
        if self.intall > self.intc:
            for i in range(31):
                self.intall4 = self.binall[1:]
                if self.intall4[i] == "1":
                    self.intall5 += "0"
                else:
                    self.intall5 += "1"
            self.intfinall1 = int(self.intall5, 2)
            self.intfinall2 = self.intfinall1 + 1
            self.intfinally = -self.intfinall2

        else:
            self.intfinally = self.intall
        return self.intfinally


if __name__ == '__main__':
    print(int_to_bit(65535, 56635))
