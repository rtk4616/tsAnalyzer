__author__ = 'Angel'

import unittest
import platform
from src.model.configurationManager import ConfigurationManager

class Test(unittest.TestCase):

    TEST_LOCALE_STRING_WINDOWS = "English_United States"
    TEST_LOCALE_STRING_DEFAULT = "en-US"

    def testConfigurationLoad(self):
        configurationManager = ConfigurationManager()
        localeString = configurationManager.getLocale()
        if platform.system() == 'Windows':
            self.assertEqual(localeString, self.TEST_LOCALE_STRING_WINDOWS)
        else:
            self.assertEqual(localeString, self.TEST_LOCALE_STRING_DEFAULT)

if __name__ == "__main__":
    unittest.main()
