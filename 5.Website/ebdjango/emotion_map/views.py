from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'site-home.html')


def about(request):
    return render(request, 'site-about.html')

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

