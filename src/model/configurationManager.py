__author__ = 'Angel'

import json
import locale

class ConfigurationManager(object):
    '''
    classdocs
    '''
    configurationPath = ''
    configurationDict = []
    LOCALE_KEY = 'locale'

    def __load(self):
        try:
            with open(self.configurationPath, 'r') as configurationFile:
                configuration = configurationFile.read()
                self.configurationDict = json.loads(configuration)

        except Exception as e:
            print '[ERROR] we couldn\'t read the configuration: ' + str(e)

    def __init__(self, configurationPath):
        self.configurationPath = configurationPath
        self.__load()

        ''' Apply configuration locale '''
        try:
            locale.setlocale(locale.LC_ALL, str(self.getLocale()))

        except Exception as e:
            print '[ERROR] we couldn\'t apply the locale: ' + str(e)
            print 'Using default locale'
            locale.setlocale(locale.LC_ALL, '')

    def getLocale(self):
        return self.configurationDict[self.LOCALE_KEY]