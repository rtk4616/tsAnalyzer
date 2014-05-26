'''
Created on May 20, 2014

@author: Angel
'''
import locale
import struct
import time
import logging
from model.packetIdentifier import PacketIdentifier
from model.programAssociationTable import ProgramAssociationTable

class DvbCPacketParser(object):
    '''
    classdocs
    '''
    DVB_C_TRANSPORT_STREAM_PACKET_SIZE = 188
    filePath = ''
    parseElapsedTime = 0
    logger = None

    ''' Parsed items '''
    packetCount = 0
    transportStreamId = 0

    def __init__(self, filePath, logger):
        '''
        Constructor
        '''
        self.filePath = filePath
        self.logger = logger

    def parse(self):
        try:
            startTime = time.time()
            with open(self.filePath, 'rb') as transportStreamFile:
                while True:
                    pointerField = 0
                    adaptationField = False
                    payload = False
                    dvbCPacket = transportStreamFile.read(self.DVB_C_TRANSPORT_STREAM_PACKET_SIZE)
                    if not dvbCPacket:
                        break
                    elif len(dvbCPacket) != self.DVB_C_TRANSPORT_STREAM_PACKET_SIZE:
                        self.logger.error('We have a packet with a size %d and not %d that shouldn\'t happen' \
                              % (len(dvbCPacket), self.DVB_C_TRANSPORT_STREAM_PACKET_SIZE))
                        break

                    packetHeader = struct.unpack('>BHB', dvbCPacket[:4])
                    adaptationField = ((packetHeader[2] & 0x20) >> 5) & 0xff
                    payload = ((packetHeader[2] & 0x10) >> 4) & 0xff
                    pointerFieldLocation = 4

                    if adaptationField:
                        self.logger.debug('Adaptation field')
                        adaptationFieldLength = struct.unpack('>B', dvbCPacket[4:5])
                        pointerFieldLocation =+ adaptationFieldLength[0]

                    packetIdNumber = packetHeader[1] & 0x1fff
                    packetId = PacketIdentifier(packetIdNumber)

                    if packetId.isPatTable():
                        self.logger.debug('PAT found')
                        if payload:
                            pointerField = struct.unpack('>B', dvbCPacket[pointerFieldLocation:pointerFieldLocation +1])
                            patTable = ProgramAssociationTable(dvbCPacket[pointerField[0] + pointerFieldLocation + 1:])
                            self.transportStreamId = patTable.getTransportStreamId()

                    self.packetCount += 1

            self.parseElapsedTime = time.time() - startTime
        except Exception:
            self.logger.error('ohh something weird happen', exc_info=True)

    def stdOutputReport(self):
        print '---------------------------------------------'
        print '             TS Analyzer Results             '
        print '---------------------------------------------'
        print ''
        print 'packet count: ' + locale.format("%d", self.packetCount, grouping=True)
        print 'transport stream Id: ' + str(self.transportStreamId)
        print ''
        print 'parsing took: ' + "{:.2f}".format(self.parseElapsedTime) + 's'
