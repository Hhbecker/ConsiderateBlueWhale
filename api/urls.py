from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('audiofiles-list/', views.fileList, name="fileList"),
    path('audiofiles-detail/<str:pk>/', views.fileDetail, name="audiofiles-detail"),
    path('audiofiles-create/', views.fileCreate, name="fileCreate"),
    path('audiofiles-update/<str:pk>/', views.fileUpdate, name="audiofiles-update"),
    path('audiofiles-delete/<str:pk>/', views.fileDelete, name="audiofiles-delete"),

]