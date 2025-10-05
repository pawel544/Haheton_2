from django.urls import path
from . import views

app_name='user'

urlpatterns=[
        path('signup/', views.signupuser, name='signupuser' ),
        path('login/',views.loginuser, name='loginuser'),
        path('logaut/', views.logautuser, name='logautuser')


]