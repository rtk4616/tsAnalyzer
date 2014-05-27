'''
Created on May 20, 2014

@author: Angel
'''

import argparse
import logging
import sys
from src.model.dvbCPacketParser import DvbCPacketParser
from src.model.configurationManager import ConfigurationManager

if __name__ == '__main__':
    logger = logging.getLogger(__name__)

    try:
        parser = argparse.ArgumentParser(prog='tsAnalyzer')
        parser.add_argument("tsRecordingPath", help="Path to the transport stream recording to parse")
        args = parser.parse_args()
        if args.tsRecordingPath:
            configManager = ConfigurationManager()

            dvbCParser = DvbCPacketParser(args.tsRecordingPath, logger)
            dvbCParser.parse()
            dvbCParser.stdOutputReport()

    except Exception:
        logging.basicConfig()
        logger.error('ohh something weird happen', exc_info=True)
        sys.exit(-1)