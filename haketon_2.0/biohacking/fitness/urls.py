from django.urls import path
from .views import *

gym_obiect = 'fitness'

urlpatterns = [
    path('', training_view, name = 'training_view'),


]