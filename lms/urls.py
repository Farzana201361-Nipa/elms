from django.urls import path 
from django.shortcuts import redirect
from . import views

app_name = "lms"
urlpatterns = [
    path('home/',views.home, name='home'),
    path('', lambda request: redirect('/home/')),
]

