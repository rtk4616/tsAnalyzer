__author__ = 'Angel'

import json

class ConfigurationManager(object):
    '''
    classdocs
    '''
    configurationPath = ''
    configurationDict = []
    LOCALE_KEY = 'locale'

    def __init__(self, configurationPath):
        self.configurationPath = configurationPath

    def load(self):
        try:
            with open(self.configurationPath, 'r') as configurationFile:
                configuration = configurationFile.read()
                self.configurationDict = json.loads(configuration)

        except Exception as e:
                print '[ERROR] we couldn\'t read the configuration: ' + str(e)

    def getLocale(self):
        return self.configurationDict[self.LOCALE_KEY]