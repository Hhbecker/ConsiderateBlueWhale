from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('audiofiles-list/', views.fileList, name="audiofiles-list"),
    path('audiofiles-detail/<str:pk>/', views.fileDetail, name="audiofiles-detail"),
    path('audiofiles-create/', views.fileCreate, name="audiofiles-create"),
    path('audiofiles-update/<str:pk>/', views.fileUpdate, name="audiofiles-update"),
    path('audiofiles-delete/<str:pk>/', views.fileDelete, name="audiofiles-delete"),

]