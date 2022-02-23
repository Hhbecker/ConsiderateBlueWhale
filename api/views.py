# A given serializer will parse information in both directions 
# (reads and writes), but the ViewSet is where the available 
# operations are defined. 

from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import AudioFile
from .serializers import AudioFileSerializer

from .models import AudioFile

# Create your views here.

# this is a decorator which allows you to specify which HTTP methods this view is allowed to respond to
@api_view(['GET'])
# view apiOverview: lists each url path the api can service - only responds to GET requests (otherwise 405 method not allowed error returned)
def apiOverview(request):

    # define the api_urls list object
    api_urls = {
        'List':'/audiofiles-list/',
        'DetailView':'fileDetail/<str:pk>/',
        'Create':'auidofile-create/',
        'Update':'audiofile-update/<str:pk>/',
        'Delete':'audiofile-delete/<str:pk>/'
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
    # return the JSON data of the AudioFile instances
    return(Response(serializer.data))

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

# view fileCreate: add an AudioFile instance to the database
@api_view(['POST'])
def fileCreate(request):
    # pass the data in the request into the serializer function
    serializer = AudioFileSerializer(data=request.data)
    # if data satisfies model requirements save it to the database
    if serializer.is_valid():
        serializer.save()
        return(Response('Audio file added to database.'))


@api_view(['POST'])
# define function based view named fileUpdate which takes in an (http?) 
# request and a primary key identifer and returns a json response
def fileUpdate(request, pk):
    # from AudioFile model (which we imported) get the object with the id 
    # equal to the pk var passed into the view function
    file = AudioFile.objects.get(id=pk)
    serializer = AudioFileSerializer(instance=file, data=request.data)
    # if the POST data is valid replace (I think replace) the current database instance with the new data
    if serializer.is_valid():
        serializer.save()
    return(Response('Audio file updated.'))

# view fileDelete: deletes AudioFile instance from database
# input: DELETE request, id of AudioFile to be deleted
@api_view(['DELETE'])
def fileDelete(request, pk):
    file = AudioFile.objects.get(id=pk)
    file.delete()
    return(Response('Audio file deleted.'))

