__author__ = 'Angel'

import locale
import logging
import platform

class ConfigurationManager(object):
    '''
    classdocs
    '''
    configurationDict = []
    logger = None
    activeLanguageDict = []

    LOCALE_KEY = 'locale'
    LOCALE_FOLDER = 'localeFolder'
    LOGGING_LEVEL = 'loggingLevel'

    defaultConfiguration = {
        LOCALE_KEY: {"Windows" : "English_United States", "Linux" : "en-US", "Default" : "en-US"},
        LOGGING_LEVEL: "INFO",
        LOCALE_FOLDER: "locale"
    }

    def __loadConfiguration(self):
        self.configurationDict = self.defaultConfiguration

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        ''' Setting logging level '''
        logging.basicConfig()

        self.__loadConfiguration()

        ''' Apply configuration locale '''
        try:
            locale.setlocale(locale.LC_ALL, str(self.getLocale()))

        except Exception:
            self.logger.error('we couldn\'t apply the locale', exc_info=True)
            self.logger.info('Using default locale')
           # locale.setlocale(locale.LC_ALL, '')



    def getLocale(self):
        localeDict = self.configurationDict[self.LOCALE_KEY]
        machineOs = platform.system()

        if machineOs == 'Windows':
            return localeDict[machineOs]
        elif machineOs == 'Linux':
            return localeDict[machineOs]
        else:
            return localeDict['Default']