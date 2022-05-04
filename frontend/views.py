from curses.ascii import HT
from django.shortcuts import render, redirect
from django.http import HttpRequest
from api import views
import json
from api.serializers import AudioFileSerializer
import requests
from rest_framework.decorators import api_view
from api.forms import AudioFileForm
from api.serializers import AudioFileSerializer

# Create your views here.

def apiOverview(request):
    return render(request, 'frontend/home.html')

def library(request):
    return render(request, 'frontend/library.html')

