__author__ = 'Angel'

import unittest
from model.configurationManager import ConfigurationManager

class Test(unittest.TestCase):

    TEST_CONFIGURATION_PATH = './../data/configuration.json'
    TEST_LOCALE_STRING = "en_GB"

    def testConfigurationLoad(self):
        configurationManager = ConfigurationManager(self.TEST_CONFIGURATION_PATH)
        configurationManager.load()
        localeString = configurationManager.getLocale()
        self.assertEqual(localeString, self.TEST_LOCALE_STRING)

if __name__ == "__main__":
    unittest.main()
