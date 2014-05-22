'''
Created on May 20, 2014

@author: Angel
'''
import locale
import struct
import time
from model.packetIdentifier import PacketIdentifier
from model.programAssociationTable import ProgramAssociationTable

class DvbCPacketParser(object):
    '''
    classdocs
    '''
    DVB_C_TRANSPORT_STREAM_PACKET_SIZE = 188
    filePath = ''
    parseElapsedTime = 0
    packetCount = 0


    def __init__(self, filePath):
        '''
        Constructor
        '''
        self.filePath = filePath

    def parse(self):
        try:
            startTime = time.time()
            with open(self.filePath, 'rb') as transportStreamFile:
                while True:
                    payloadStart = 0
                    adaptationField = False
                    dvbCPacket = transportStreamFile.read(self.DVB_C_TRANSPORT_STREAM_PACKET_SIZE)
                    if not dvbCPacket:
                        break
                    elif len(dvbCPacket) != self.DVB_C_TRANSPORT_STREAM_PACKET_SIZE:
                        print '[ERROR] We have a packet with a size %d and not %d that shouldn\'t happen' \
                              % (len(dvbCPacket), self.DVB_C_TRANSPORT_STREAM_PACKET_SIZE)
                        break

                    packetHeader = struct.unpack('>BHB', dvbCPacket[:4])

                    if adaptationField:
                        adaptationFieldLength = struct.unpack('>B', dvbCPacket[4:5])
                        print 'adaptationFieldLength ' + str(adaptationFieldLength[0])

                    packetIdNumber = packetHeader[1] & 0x1fff
                    packetId = PacketIdentifier(packetIdNumber)

                    if packetId.isPatTable():
                        print 'PAT found'
                        if payloadStart:
                            ProgramAssociationTable(dvbCPacket[payloadStart:])


                    self.packetCount += 1

            self.parseElapsedTime = time.time() - startTime
        except Exception as e:
            print '[ERROR] ohh something weird happen: ' + str(e)

    def stdOutputReport(self):
        print '---------------------------------------------'
        print '             TS Analyzer Results             '
        print '---------------------------------------------'
        print ''
        print 'packet count: ' + locale.format("%d", self.packetCount, grouping=True)
        print ''
        print 'parsing took: ' + "{:.2f}".format(self.parseElapsedTime) + 's'
