__author__ = 'Angel'


import unittest
from model.packetIdentifier import PacketIdentifier

class Test(unittest.TestCase):

    def testPidTypes(self):

        packetId = PacketIdentifier(0)
        self.assertTrue(packetId.isPatTable())
        packetId = PacketIdentifier(1)
        self.assertTrue(packetId.isCatTable())
        packetId = PacketIdentifier(2)
        self.assertTrue(packetId.isTsdtTable())
        packetId = PacketIdentifier(3)
        self.assertTrue(packetId.isIpmpTable())
        packetId = PacketIdentifier(58)
        self.assertTrue(packetId.isPmtTable())

if __name__ == "__main__":
    unittest.main()