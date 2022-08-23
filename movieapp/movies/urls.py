from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),   
    path("movies", views.movies),
    path("movies/<slug:slug>", views.movie_details, name="movie_details")
]
