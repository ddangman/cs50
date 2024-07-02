"""
This file is just responsible for URLs
and directing users to what should happen when those URLs are clicked
"""

from django.urls import path

# from . means from current directory
from . import views

urlpatterns = [
    # call to views.py functions in same directory
    path("", views.index1, name="index"), # empty string after route
    path("<str:name>", views.greet1, name="greet"), # variable str after route
    # explicitly defined route str
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david"),
]
