__author__ = 'Angel'


import unittest
import struct
from src.model.programAssociationTable import ProgramAssociationTable

class Test(unittest.TestCase):

    PAT_CONTENT_EXAMPLE = struct.pack(">BBBBB", 0x00, 0xB0, 0x29, 0x00, 0x0B)
    TRANSPORT_STREAM_ID = 11

    def testGetTransportStreamId(self):
        pat = ProgramAssociationTable(self.PAT_CONTENT_EXAMPLE)
        self.assertEqual(pat.getTransportStreamId(), self.TRANSPORT_STREAM_ID)

if __name__ == "__main__":
    unittest.main()