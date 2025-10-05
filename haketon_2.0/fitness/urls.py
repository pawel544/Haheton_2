from django.urls import path
from .views import *

app_name = 'fitness'

urlpatterns = [
    path('', training_view, name = 'training_view'),


]