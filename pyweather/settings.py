# coding=UTF-8
import ConfigParser
import data
import fetchTemp

# Global variables set by configs
city = ""
language = ""

# Function that will read config file and set variables accordingly
def read_cfg():
    config = ConfigParser.RawConfigParser()
    config.read('settings.cfg')

    global city, language
    city = config.get("Settings","city")
    language = config.get("Settings","language")

    if not city:
        city = config.get("Default", "city")
    if not language:
        language = config.get("Default", "language")


    #read_cfg()
    #lookup_url = data.dictionary[city.decode('utf-8')]
    #print fetchTemp.get_temperature(lookup_url)

