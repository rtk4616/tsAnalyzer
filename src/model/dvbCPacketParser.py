'''
Created on May 20, 2014

@author: Angel
'''
import locale
import struct
from model.packetIdentifier import PacketIdentifier

class DvbCPacketParser(object):
    '''
    classdocs
    '''
    DVB_C_TRANSPORT_STREAM_PACKET_SIZE = 188
    filePath = ''
    packetCount = 0


    def __init__(self, filePath):
        '''
        Constructor
        '''
        self.filePath = filePath

    def parse(self):
        try:
            with open(self.filePath, 'rb') as transportStreamFile:
                while True:
                    dvbCPacket = transportStreamFile.read(self.DVB_C_TRANSPORT_STREAM_PACKET_SIZE)
                    if not dvbCPacket:
                        break
                    elif len(dvbCPacket) != self.DVB_C_TRANSPORT_STREAM_PACKET_SIZE:
                        print '[ERROR] We have a packet with a size %d and not %d that shouldn\'t happen' \
                              % (len(dvbCPacket), self.DVB_C_TRANSPORT_STREAM_PACKET_SIZE)
                        break

                    packetHeader = struct.unpack('>BH', dvbCPacket[:3])
                    packetIdNumber = packetHeader[1] & 0x1fff
                    packetId = PacketIdentifier(packetIdNumber)
                    # print 'packetIdNumber ' + str(packetIdNumber)

                    if packetId.isPatTable():
                        print 'PAT found'

                    self.packetCount += 1

        except Exception as e:
            print '[ERROR] ohh something weird happen: ' + str(e)

    def stdOutputReport(self):
        print '---------------------------------------------'
        print '             TS Analyzer Results             '
        print '---------------------------------------------'
        print ''
        print 'packet count: ' + locale.format("%d", self.packetCount, grouping=True)
