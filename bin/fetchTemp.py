import xml.dom.minidom 
import string
import urllib2
import sys
import Cities

## Fetches appropriate info from Environment Canada RSS Feed and formats output
def getTemp(data):
	nodelist = data.getElementsByTagName("title")
	for node in nodelist:
		if "Current Conditions:" in node.firstChild.nodeValue:
			s = string.split(node.firstChild.nodeValue, ": ", -1)
			print s[1]

#
city = sys.argv[1]
req = urllib2.Request(Cities.cities[city])
response = urllib2.urlopen(req)
xml = xml.dom.minidom.parseString(response.read())
getTemp(xml)