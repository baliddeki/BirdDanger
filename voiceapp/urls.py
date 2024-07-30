from django.urls import path
from . import views

urlpatterns = [
    # defining the urls
    path('upload/', views.upload_voice, name='upload_voice'),
    path('list/', views.voice_list, name='voice_list')
]

