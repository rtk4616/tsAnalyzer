__author__ = 'Angel'

class PacketIdentifier(object):
    PAT = 0
    CAT = 1
    TSDT = 2
    IPMP = 3
    PMT_FIRST_INTERVAL_LOWER_LIMIT = 32
    PMT_FIRST_INTERVAL_HIGHER_LIMIT = 8186
    PMT_SECOND_INTERVAL_LOWER_LIMIT = 8188
    PMT_SECOND_INTERVAL_HIGHER_LIMIT = 8190

    pidValue = 0

    def __init__(self, pidValue):
        self.__pidValue = pidValue

    def isPatTable(self):
        return True if self.__pidValue == self.PAT else False

    def isCatTable(self):
        return True if self.__pidValue == self.CAT else False

    def isTsdtTable(self):
        return True if self.__pidValue == self.TSDT else False

    def isIpmpTable(self):
        return True if self.__pidValue == self.IPMP else False

    def isPmtTable(self):
        if (((self.__pidValue >= self.PMT_FIRST_INTERVAL_LOWER_LIMIT) and
            (self.__pidValue <= self.PMT_FIRST_INTERVAL_HIGHER_LIMIT)) or
            ((self.__pidValue >= self.PMT_SECOND_INTERVAL_LOWER_LIMIT) and
            (self.__pidValue <= self.PMT_SECOND_INTERVAL_HIGHER_LIMIT))):

            return True
        else:
            return False