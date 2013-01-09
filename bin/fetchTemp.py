import xml.dom.minidom 
import string
import urllib2
import Cities

## Looks up city in dictionnary for URL,
## @return xml data
def getData(city):
	req = urllib2.Request(Cities.cities[city])
	response = urllib2.urlopen(req)
	data = xml.dom.minidom.parseString(response.read())
	return data

## Fetches appropriate info from Environment Canada RSS Feed and formats output
## @return [condition] temperature
def getTemp(city):
	data = getData(city)
	nodelist = data.getElementsByTagName("title")
	for node in nodelist:
		if "Current Conditions:" in node.firstChild.nodeValue:
			s = string.split(node.firstChild.nodeValue, ": ", -1)
			data.unlink()
			return s[1]