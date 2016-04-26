from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pymongo
import os
from .models import Greeting
import json
import calendar
import datetime

# Create your views here.
def index(request):

        countriesFile = os.path.join(os.path.dirname(__file__), '..', 'ebdjango/static/countriesISOA2.geojson')
        countriesFile= os.path.normpath(countriesFile)

        with open(countriesFile) as f:  # this is a master file with boundaries for all countries
            allCountries = json.load(f)


        # create an instance of the Mongodb client with a connection to our database on Mongolab.
        client = pymongo.MongoClient("ds019980.mlab.com",19980, connect=False)

        # create a database called worldemotion
        db=client['worldemotion']

        #access the collection
        collection=db['countryEmotion']

        # MongoLab has user authentication
        db.authenticate("5Vs", "bigdata2016")
        times = collection.find()


        # finding the most recent collection by comparison of timestamps
        timestamps = []
        collections = []
        for time in times:
            timestamp = time['country_emotion'][0]['current_time']
            print timestamp
            day_of_week = (timestamp[0:4])
            month_abbr = timestamp[4:7]
            month = list(calendar.month_abbr).index(month_abbr)
            day = int(timestamp[7:10])
            hour = int(timestamp[11:13])
            minute = int(timestamp[14:16])
            second = int(timestamp[17:19])
            year = int(timestamp[20:25])

            timestamps.append(datetime.datetime(year, month, day, hour, minute, second))
            collections.append(time['country_emotion'])


        most_recent = collections[timestamps.index(max(timestamps))]

        #  initiate a dictionary object to be written to a geojson file
        moodyCountriesGeoJson = {"type": "FeatureCollection", "features": []}

        for country in most_recent[1:]:
             for feature in allCountries['features']:
                 if feature['properties']['ISO_A2'] == country['country']:
                     feature['properties']['mood'] = country['emotion']
                     moodyCountriesGeoJson['features'].append(feature)


        outputFile = os.path.join(os.path.dirname(__file__), '..', 'ebdjango/static/countries_with_moods2.geojson')
        outputFile = os.path.normpath(outputFile)

        with open(outputFile, 'w') as f:
            f.write(json.dumps(moodyCountriesGeoJson, indent=3))

        return render(request, 'site-home.html', {'timestamp': most_recent[0]['current_time']})


def about(request):
    return render(request, 'site-about.html')

def ibm(request):
    return render(request, 'ibm-aggregation.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

