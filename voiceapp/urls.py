from django.urls import path
from . import views

urlpatterns = [
    # defining the urls
    path('', views.upload_voice, name='index'),  # Set the index page
    path('list/', views.voice_list, name='voice_list')
]

