__author__ = 'Angel'

import unittest
import locale
from model.dvbCPacketParser import DvbCPacketParser

class Test(unittest.TestCase):

    TRANSPORT_STREAM_RECORDING_PATH_1 = './../data/synopsis2.ts'

    def setUp(self):
        locale.setlocale(locale.LC_ALL, 'English_United States.1252')

    def testSimpleParse(self):
        packetParser = DvbCPacketParser(self.TRANSPORT_STREAM_RECORDING_PATH_1)
        packetParser.parse()
        packetParser.stdOutputReport()

if __name__ == "__main__":
    unittest.main()