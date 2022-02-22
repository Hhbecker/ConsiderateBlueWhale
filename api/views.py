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
