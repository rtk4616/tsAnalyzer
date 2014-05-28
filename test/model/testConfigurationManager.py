__author__ = 'Angel'

import unittest
from src.model.configurationManager import ConfigurationManager

class Test(unittest.TestCase):

    TEST_LOCALE_STRING = "English_United States.1252"

    def testConfigurationLoad(self):
        configurationManager = ConfigurationManager()
        localeString = configurationManager.getLocale()
        self.assertEqual(localeString, self.TEST_LOCALE_STRING)

if __name__ == "__main__":
    unittest.main()
