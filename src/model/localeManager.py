__author__ = 'Angel'

'''
Not a fan of putting data and code together but in this case I want to be able to pack
code and text messages inside the same exe and I couldn't find a way to do it using p2exe
unless the data is part of the code modules.
'''
class localeManager(object):

    messages = {
                "ARGUMENT_PARSER_MESSAGE": "Path to the transport stream recording to parse"
               }

    def getText(self, stringKey):
      if self.messages.has_key(stringKey):
          return self.messages[stringKey]
      else:
          return stringKey