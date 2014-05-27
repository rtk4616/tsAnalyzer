__author__ = 'Angel'

import json
import locale
import logging

class ConfigurationManager(object):
    '''
    classdocs
    '''
    configurationDict = []
    logger = None
    LOCALE_KEY = 'locale'

    defaultConfiguration = {
        "locale": "English_United States.1252",
        "loggingLevel": "INFO"
    }

    def __load(self):
        self.configurationDict = self.defaultConfiguration

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.__load()

        ''' Setting logging level '''
        logging.basicConfig()

        ''' Apply configuration locale '''
        try:
            locale.setlocale(locale.LC_ALL, str(self.getLocale()))

        except Exception:
            self.logger.error('we couldn\'t apply the locale', exc_info=True)
            self.logger.info('Using default locale')
            locale.setlocale(locale.LC_ALL, '')

    def getLocale(self):
        return self.configurationDict[self.LOCALE_KEY]