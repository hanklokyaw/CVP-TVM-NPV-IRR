import math

class CVP:

    def __init__(self, pv, fv, rate, nper, pmt):
        super().__init__()
        self.pv = pv
        self.fv = fv
        # note rate is in decimal such as 0.01 for 1% or 0.5 for 50%
        self.rate = rate
        self.nper = nper
        self.pmt = pmt

    def PV(self):
        self.pv = self.fv / (1 + self.rate) ** self.nper
        return self.pv

    def FV(self):
        self.fv = self.pv * (1 + self.rate) ** self.nper
        return self.fv

    def RATE(self):
        self.rate = (math.pow((self.fv/self.pv),1/self.nper)) - 1
        return self.rate

    def NPER(self):
        self.nper = math.log(self.fv/self.pv, 1+self.rate)
        return self.nper

    def PMT(self):
        pass





