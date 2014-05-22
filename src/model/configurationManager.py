__author__ = 'Angel'

import json
import locale
import logging

class ConfigurationManager(object):
    '''
    classdocs
    '''
    configurationPath = ''
    configurationDict = []
    logger = None
    LOCALE_KEY = 'locale'

    def __load(self):
        try:
            with open(self.configurationPath, 'r') as configurationFile:
                configuration = configurationFile.read()
                self.configurationDict = json.loads(configuration)

        except Exception:
            self.logger.error('We couldn\'t read the configuration', exc_info=True)

    def __init__(self, configurationPath):
        self.logger = logging.getLogger(__name__)
        self.configurationPath = configurationPath
        self.__load()

        ''' Apply configuration locale '''
        try:
            locale.setlocale(locale.LC_ALL, str(self.getLocale()))

        except Exception:
            self.logger.error('we couldn\'t apply the locale', exc_info=True)
            self.logger.info('Using default locale')
            locale.setlocale(locale.LC_ALL, '')

        ''' Setting logging level '''


    def getLocale(self):
        return self.configurationDict[self.LOCALE_KEY]