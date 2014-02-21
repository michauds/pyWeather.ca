## load data into dictionary

import json

dictionary = {}

def load():
    with open('canada.json', 'rb') as city_list:
        global dictionary
        json.load(city_list)
        print dictionary[Montreal]
        

load()
