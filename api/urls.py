
# specifies which views should be called when a given url is requested

from django.urls import path
from . import views

urlpatterns = [
    # URL pattern has three components:
    # 1. The addition to the base url of the site
    # 2. The view function you would like to be called when that url (base+addition) is requested
    # 3. The name of the ______________________ html page that should be called?

    # base URL is 'api/' 

    # call the apiOverview view
    path('', views.apiOverview, name="overview"),
    # call the fileList view
    path('list/', views.fileList, name="list"),
    path('listJson/', views.frontendList, name="frontendList"),
    # call the fileDetail view when the 'api/detail/<str:pk>/' url is requested
    path('detail/<str:pk>/', views.fileDetail, name="detail"),
    # call the fileCreate view when the 'api/create/' url is requested
    path('create/', views.fileCreate, name="create"),
    path('fileUpload/', views.fileUpload, name="fileUpload"),
    #
    path('list/update/<str:pk>/', views.fileUpdate, name="update"),
    #
    path('list/delete/<str:pk>/', views.fileDelete, name="delete"),

]