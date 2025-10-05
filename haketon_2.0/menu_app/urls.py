from django.urls import path
from .views import *

app_name = 'menu_app'

urlpatterns = [
    path('', menu, name = 'menu')]