import csv
import json
import os
import sys

def convert():
    with open(os.path.join(sys.path[0], "countries.geojson")) as f:
        countries = json.load(f)


    with open(os.path.join(sys.path[0], "iso_a2_to_a3.csv")) as csvfile:
        dic = {}
        reader = csv.reader(csvfile, delimiter =',')
        for row in reader:
            dic.update({row[1]:row[0]})


    for c in countries['features']:
        ISO_A3 =  c['properties']['ISO_A3']

        try:
             c['properties']['ISO_A2'] = dic[ISO_A3]
        except:
            c['properties']['ISO_A2'] = "nil"


    with open(os.path.join(sys.path[0], "countriesISOA2.geojson"), "w") as f:
        f.write(json.dumps(countries, indent=2))

convert()