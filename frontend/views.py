from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpRequest
from api import views
import json
from api.serializers import AudioFileSerializer
import requests

# Create your views here.

def apiOverview(request):
    return render(request, 'frontend/home.html')

def library(request):
    return render(request, 'frontend/library.html')

def upload(request):
    # if get then return form 

    # if post then serialize form data into a json object and send it as a post request to the api
    # http://127.0.0.1:8000/api/create
    # response = request.post('http://127.0.0.1:8000/')


    # need to add model and form pages from api app to this app
    return render(request, 'frontend/upload.html')

def update(request):
    return render(request, 'frontend/update.html')
