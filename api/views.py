import re
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import AudioFile
from .serializers import AudioFileSerializer

from .models import AudioFile
# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List':'/audiofiles-list/',
        'DetailView':'fileDetail/<str:pk>/',
        'Create':'auidofile-create/',
        'Update':'audiofile-update/<str:pk>/',
        'Delete':'audiofile-delete/<str:pk>/'
    }

    return JsonResponse(api_urls)

@api_view(['GET'])
def fileList(request):
    files = AudioFile.objects.all()
    serializer = AudioFileSerializer(files, many = True)
    return(Response(serializer.data))

@api_view(['GET'])
def fileDetail(request, pk):
    files = AudioFile.objects.get(id=pk)
    serializer = AudioFileSerializer(files, many = False)
    return(Response(serializer.data))

@api_view(['POST'])
def fileCreate(request):
    serializer = AudioFileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return(Response(serializer.data))


# POST decorator which ____
@api_view(['POST'])
# define function based view named fileUpdate which takes in an (http?) 
# request and a primary key identifer and returns a json response
def fileUpdate(request, pk):
    # from AudioFile model (which we imported) get the object with the id 
    # equal to the pk var passed into the view function
    file = AudioFile.objects.get(id=pk)
    serializer = AudioFileSerializer(instance=file, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return(Response(serializer.data))

@api_view(['DELETE'])
def fileDelete(request, pk):
    file = AudioFile.objects.get(id=pk)
    file.delete()
    return(Response('Audio File Deleted'))

