from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Greeting

# Create your views here.


def index(request):
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def about(request):
    return render(request, "about.html")


def dashboard(request):
    return render(request, "dashboard.html")
