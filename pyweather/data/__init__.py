# load data into dictionary

import json, os

dictionary = {}

	 

def load():
    json_path = os.path.abspath('.')
    if "data" not in json_path:
       json_path = os.path.join(json_path, 'data/')
 
    with open(os.path.join(json_path,'canada.json'), 'rb') as city_list:
        global dictionary 
	dictionary = json.load(city_list, encoding="utf-8")
        
load()
