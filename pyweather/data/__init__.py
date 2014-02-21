# load data into dictionary

import json

dictionary = {}

def load():
    with open('canada.json', 'rb') as city_list:
        global dictionary 
	dictionary = json.load(city_list, encoding="utf-8")
        
load()
