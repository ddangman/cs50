from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # default page
    path("sections/<int:num>", views.section, name="section") # section page
]