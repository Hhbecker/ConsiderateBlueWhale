from django.shortcuts import render

# Create your views here.

def apiOverview(request):
    return render(request, 'frontend/home.html')

def library(request):
    return render(request, 'frontend/library.html')
