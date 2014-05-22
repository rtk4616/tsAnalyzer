__author__ = 'Angel'

class PID():
    PAT = 0
    CAT = 1
    TSDT = 2
    IPMP = 3
    pidValue = 0

    def __init__(self, pidValue):
        self.pidValue = pidValue

    def isPatTable(self):
        return True if self.pidValue == self.PAT else False

    def isCatTable(self):
        return True if self.pidValue == self.CAT else False

    def isTsdtTable(self):
        return True if self.pidValue == self.TSDT else False

    def isIpmpTable(self):
        return True if self.pidValue == self.IPMP else False
