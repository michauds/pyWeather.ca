#!/usr/bin/python

import csv, json, cStringIO

dictionary = {}

with open('data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)

    for rows in reader:
        dictionary[rows[1]] = rows[2]

with open('city_dictionary.json', 'w') as output:
    output.write(json.dumps(dictionary))
