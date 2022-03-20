# Implements the functions called when the urls designated in urls.py are requested  

# A given serializer will parse information in both directions 
# (reads and writes), but the ViewSet is where the available 
# operations are defined. 

import re
from django.http import JsonResponse
from django.shortcuts import redirect, render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import AudioFile
from .serializers import AudioFileSerializer

from .models import AudioFile
from .forms import AudioFileForm
import librosa as lib
import pathlib

# current working directory
print(pathlib.Path().absolute())

def getBpm(filePath):
    # confirm input is valid audio file with positive duration

    y,sr = lib.load(filePath)

    if lib.util.valid_audio(y):
        #length = lib.get_duration(audioFile) 
        onset_env = lib.onset.onset_strength(y=y, sr=sr)
        tempo = lib.beat.tempo(onset_envelope=onset_env, sr=sr)
        return tempo[0]
    else:
        return -1

# this is a decorator which allows you to specify which HTTP methods this view is allowed to respond to
@api_view(['GET'])
# view apiOverview: lists each url path the api can service - only responds to GET requests (otherwise 405 method not allowed error returned)
def apiOverview(request):

    # define the api_urls list object
    api_urls = {
        'List':'/list/',
        'Detail':'/detail/<str:pk>/',
        'Create':'/create/',
        'Update':'/update/<str:pk>/',
        'Delete':'/delete/<str:pk>/'
    }

    # return the api_urls list object packaged in JSON format by the JsonResponse function
    return JsonResponse(api_urls)


# view fileList: lists all fields of each AudioFile instance - only responds to GET requests
@api_view(['GET'])
def fileList(request):
    # define the file variable which contains all instances of the AudioFile class in the database 
    files = AudioFile.objects.all() 
    # serialize all of the AudioFile instances into JSON using the AudioFileSerializer function imported from serializers.py
    serializer = AudioFileSerializer(files, many = True)
    # render function: takes in path to html file and saves the files variable into a variable that can be manipulated in the html
    # I would ideally use the serialized version of the AudioFile objects but I can't get it to work.
    return render(request, 'api/fileList.html', {'files' : files})

    # view fileList: lists all fields of each AudioFile instance - only responds to GET requests
@api_view(['GET'])
def frontendList(request):
    # define the file variable which contains all instances of the AudioFile class in the database 
    files = AudioFile.objects.all()
    # serialize all of the AudioFile instances into JSON using the AudioFileSerializer function imported from serializers.py
    serializer = AudioFileSerializer(files, many = True)
    # render function: takes in path to html file and saves the files variable into a variable that can be manipulated in the html
    # I would ideally use the serialized version of the AudioFile objects but I can't get it to work.
    return JsonResponse(serializer.data, safe=False)

# view fileCreate: add an AudioFile instance to the database
@api_view(['GET','POST'])
def fileCreate(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid:

            instance = form.save()
            bpm = getBpm(instance.file.name) 

            instance.bpm = bpm

            instance.save()
            return redirect('create')
    else:
        form = AudioFileForm()
    return render(request, 'api/fileCreate.html', {'form':form})

@api_view(['GET','POST'])
# define function based view named fileUpdate which takes in an (http?) 
# request and a primary key identifer and returns a json response
def fileUpdate(request, pk):
    if request.method == 'POST':
        # from AudioFile model (which we imported) get the object with the id 
        # can also do this in serializer 'serializer = AudioFileSerializer(instance=file, data=request.data)'
        fileObj = AudioFile.objects.get(id=pk)

        print("\n\n\n File path before update: ", fileObj.file.name, "\n Current BPM: ", fileObj.bpm, "\n\n\n")

        form = AudioFileForm(request.POST, request.FILES, instance=fileObj)
        if form.is_valid():
            # create an instance of the database object just saved
            instance = form.save()
            bpm = getBpm(instance.file.name) 
            instance.bpm = bpm
            instance.save()
            print("\n\n\n File path after update: ", instance.file.name, "\n New BPM: ", instance.bpm, "\n\n\n")

            files = AudioFile.objects.all()
            # need to change url by making get call to fileList instead of just displaying file list html
            return redirect(fileList)

    else: 
        file = AudioFile.objects.get(id=pk)
        form = AudioFileForm()
        return render(request, 'api/fileUpdate.html', {'form':form, 'file':file})
        

# view fileDelete: deletes AudioFile instance from database
# input: DELETE request, id of AudioFile to be deleted
@api_view(['DELETE'])
def fileDelete(request, pk):
    file = AudioFile.objects.get(id=pk)
    file.delete()
    files = AudioFile.objects.all()
    # serialize all of the AudioFile instances into JSON using the AudioFileSerializer function imported from serializers.py
    serializer = AudioFileSerializer(files, many = True)
    # render function: takes in path to html file and saves the files variable into a variable that can be manipulated in the html
    # I would ideally use the serialized AudioFile objects but I can't get it to work
    return render(request, 'api/fileList.html', {'files' : files})





# view fileDetail: returns all fields of a specific AudioFile instance - only responds to GET requests  
# input: GET request, id of AudioFile to be retrieved
@api_view(['GET'])
def fileDetail(request, pk):
    # save the AudioFile instance with the id = pk into the files variable 
    file = AudioFile.objects.get(id=pk)
    # serialize the AudioFile data to JSON
    serializer = AudioFileSerializer(file, many = False)
    # return the AudioFile data as JSON
    return(Response(serializer.data))
