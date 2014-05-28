__author__ = 'Angel'

import unittest
import locale
import logging
from model.dvbCPacketParser import DvbCPacketParser

class Test(unittest.TestCase):

    TRANSPORT_STREAM_RECORDING_PATH_1 = './test/data/transportStreamWithPatAndTsId.ts'
    logger = None

    def setUp(self):
        locale.setlocale(locale.LC_ALL, 'English_United States.1252')
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG)


    def testSimpleParse(self):
        packetParser = DvbCPacketParser(self.TRANSPORT_STREAM_RECORDING_PATH_1, self.logger)
        packetParser.parse()
 #       packetParser.stdOutputReport()

if __name__ == "__main__":
    unittest.main()