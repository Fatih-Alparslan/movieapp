from datetime import date
from django.shortcuts import render, HttpResponse


data= {
     "movies": [
          {
               "title": "film adı 1",
               "description": "açıklama 1",
               "imageUrl": "m1.jpg",
               "coverImage": "cover.jpg",
               "slug": "film-adi-1",
               "language": "english",
               "date": date(2022,2,2)
          },
          {
               "title": "film adı 2",
               "description": "açıklama 2",
               "imageUrl": "m2.jpg",
               "coverImage": "cover2.jpg",
               "slug": "film-adi-2",
               "language": "english",
               "date": date(2022,2,25)
          },
          {
               "title": "film adı 3",
               "description": "açıklama 3",
               "imageUrl": "m3.jpg",
               "coverImage": "cover2.jpg",
               "slug": "film-adi-3",
               "language": "türkçe",
               "date": date(2022,2,2)
          },
          {
               "title": "film adı 4",
               "description": "açıklama 4",
               "imageUrl": "m4.jpg",
               "coverImage": "cover3.jpg",
               "slug": "film-adi-4",
               "language": "english",
               "date": date(2022,2,15)
          },

     ],
     "sliders":[
          {
               "slider_image":"slider1.jpg",
               "url": "film-adi-1"      
          },
          {
               "slider_image":"slider2.jpg",
               "url": "film-adi-2"      
          },
          {
               "slider_image":"slider3.jpg",
               "url": "film-adi-3"      
          },
      
     ]
}
# Create your views here.

def index(request):
     movies=data["movies"][-4:]
     sliders=data["sliders"]
     return render(request, 'index.html',{
          "movies": movies,
          "sliders": sliders
     })

def movies(request):
     movies=data["movies"]
     return render(request, 'movies.html',{
          "movies": movies
     })


def movie_details(request,slug):
     movies=data["movies"]
     #selectedMovie = None
     #for movie in movies:
      #    if movie["slug"] == slug:
       #        selectedMovie = movie
     selectedMovie = next(movie for movie in movies if movie["slug"] == slug)


     return render(request, 'movie-details.html', {"movie": selectedMovie})