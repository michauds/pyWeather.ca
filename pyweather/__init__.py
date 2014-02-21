__title__ = 'weather_man'
__version__ = '0.1'
__author__ = 'Stephan Michaud'

import ConfigParser

# Global variables set by configs
city = "test"
language = ""

# Function that will read config file and set variables accordingly
def read_cfg():
    config = ConfigParser.RawConfigParser()
    config.read('settings.cfg')
    
    global city, language
    city = config.get("Settings","city")
    language = config.get("Settings","language")

    if city is None:
        city = config.get("Defaults", "city")
    if language is None:
        language = config.get("Defaults", "language")




read_cfg()
print city
print language

