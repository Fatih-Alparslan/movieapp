from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home_page"),   
    path("movies", views.movies, name="movie_page"),
    path("movies/<slug:slug>", views.movie_details, name="movie_details")
]
