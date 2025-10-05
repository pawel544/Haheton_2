from django.urls import path
from .views import diet_views

app_name = 'diet_app'

urlpatterns=[
    path('', diet_views , name = 'diet_views')
]