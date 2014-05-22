__author__ = 'Angel'

import unittest
from model.dvbCPacketParser import DvbCPacketParser

class Test(unittest.TestCase):

    TRANSPORT_STREAM_RECORDING_PATH_1 = './../data/synopsis2.ts'

    def testSimpleParse(self):
        packetParser = DvbCPacketParser(self.TRANSPORT_STREAM_RECORDING_PATH_1)
        packetParser.parse()
        packetParser.stdOutputReport()

if __name__ == "__main__":
    unittest.main()