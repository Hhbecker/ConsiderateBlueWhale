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

######
    # if get then return form 

    # if post then serialize form data into a json object and send it as a post request to the api
    # http://127.0.0.1:8000/api/create
    # response = request.post('http://127.0.0.1:8000/')


    # need to add model and form pages from api app to this app
    #return render(request, 'frontend/upload.html')

# view fileCreate: add an AudioFile instance to the database

# Would it be better to do all of this in javascript? (including POST request of JSON payload)
@api_view(['GET','POST'])
def upload(request):
    if request.method == 'POST':
        # place post data into form variable
        form = AudioFileForm(request.POST, request.FILES)

        if form.is_valid:
            # save form data as an instance of the model 
            instance = form.save()


##############
            # what type is instance? what type does it need to be to be serialized? 
##############



            # serialize the data into JSON
            serializer = AudioFileSerializer(instance, many = False)
            print(serializer)
            # if the serialzied data is valid send it to the upload api endpoint
            if serializer.is_valid():
                print("\n\n\n\n made it to frontend post request boiiii\n\n\n")
                response = request.POST('http://127.0.0.1:8000/api/fileUpload/', json=serializer.data) # should it be serializer.data?

                return redirect('library')
    else:
        form = AudioFileForm()
    return render(request, 'frontend/upload.html', {'form':form})

def update(request):
    return render(request, 'frontend/update.html')
