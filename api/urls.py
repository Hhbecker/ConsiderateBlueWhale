
# specifies which views should be called when a given url is requested

from django.urls import path
from . import views

urlpatterns = [
    # URL pattern has three components:
    # 1. The addition to the base url of the site
    # 2. The view function you would like to be called when that url (base+addition) is requested
    # 3. The name of the ______________________ html page that should be called?

    # base URL is 'api/' 

    # call the apiOverview view when the base url is requested ('api/')
    path('', views.apiOverview, name="api-overview"),
    # call the fileList view when the 'api/audiofiles-list/' url is requested
    path('audiofiles-list/', views.fileList, name="fileList"),
    # call the fileDetail view when the 'api/audiofiles-detail/<str:pk>/' url is requested
    path('audiofiles-detail/<str:pk>/', views.fileDetail, name="audiofiles-detail"),
    # call the fileCreate view when the 'api/audiofiles-create' url is requested
    path('audiofiles-create/', views.fileCreate, name="fileCreate"),
    #
    path('audiofiles-update/<str:pk>/', views.fileUpdate, name="audiofiles-update"),
    #
    path('audiofiles-delete/<str:pk>/', views.fileDelete, name="audiofiles-delete"),

]