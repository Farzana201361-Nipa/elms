from django.urls import path 
from . import views

app_name = "lms"
urlpatterns = [
    path('home/',views.home, name='home'),
]
