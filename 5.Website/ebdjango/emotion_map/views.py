from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pymongo

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'site-home.html')


def about(request):
     # create an instance of the Mongodb client with a connection to our database on Mongolab.
    client = pymongo.MongoClient("ds019980.mlab.com",19980)

    # create a database called worldemotion
    db=client['worldemotion']

    #access the collection
    collection=db['emotions']

    # MongoLab has user authentication
    db.authenticate("5Vs", "bigdata2016")

    # just get the first one in the collection for testing
    p = collection.find()

    locations = {}
    for tweet in p:
        locations.update({tweet['location_name']:tweet['tweet_emotion']})

    template = loader.get_template('site-about.html')
    context = {
        'locations': locations
    }
    return HttpResponse(template.render(context, request))

def US(request):
    return render(request, 'US.html')

def Australia(request):
    return render(request, 'Australia.html')

def UK(request):
    return render(request, 'UK.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

