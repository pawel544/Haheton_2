from django.urls import path
from .views import *

app_name = 'photo_rating'

urlpatterns = [
    path('', upload_training_photo, name = 'upload_training_photo'),


]


