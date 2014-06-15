__author__ = 'Angel'

import json
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
        LOCALE_FOLDER: "translations"
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
           # locale.setlocale(locale.LC_ALL, '')

        ''' Reading language '''
        try:
            with open(self.configurationDict[self.LOCALE_FOLDER] + "/" + "default.json") as languageFile:
                self.activeLanguageDict = json.load(languageFile)

        except Exception:
            self.logger.error('we couldn\'t find the language translations', exc_info=True)

    def getLocale(self):
        localeDict = self.configurationDict[self.LOCALE_KEY]
        machineOs = platform.system()

        if machineOs == 'Windows':
            return localeDict[machineOs]
        elif machineOs == 'Linux':
            return localeDict[machineOs]
        else:
            return localeDict['Default']