'''
Created on May 20, 2014

@author: Angel
'''

class DvbCPacketParser(object):
    '''
    classdocs
    '''
    DVB_C_TRANSPORT_STREAM_PACKET_SIZE = 188
    filePath = ''


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

        except Exception as e:
            print '[ERROR] ohh something weird happen: ' + str(e)