__author__ = 'Angel'

import struct

class ProgramAssociationTable(object):

    TRANSPORT_STREAM_ID_POSITION = 3
    __rawData = ''

    def __init__(self, rawData):
        self.__rawData = rawData

    def getTransportStreamId(self):
        if len(self.__rawData) > self.TRANSPORT_STREAM_ID_POSITION:
            tSIdData = self.__rawData[self.TRANSPORT_STREAM_ID_POSITION:self.TRANSPORT_STREAM_ID_POSITION + 2]
            return struct.unpack('>H', tSIdData)[0]
        else:
            return -1
