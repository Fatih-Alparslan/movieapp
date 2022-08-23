from datetime import date
from django.shortcuts import render, HttpResponse


data= {
     "movies": [
          {
               "title": "film adı 1",
               "description": "açıklama 1",
               "imageUrl": "m1.jpg",
               "slug": "film-adi-1",
               "language": "english",
               "date": date(2022,2,2)
          },
          {
               "title": "film adı 2",
               "description": "açıklama 2",
               "imageUrl": "m2.jpg",
               "slug": "film-adi-2",
               "language": "english",
               "date": date(2022,2,25)
          },
          {
               "title": "film adı 3",
               "description": "açıklama 3",
               "imageUrl": "m3.jpg",
               "slug": "film-adi-3",
               "language": "türkçe",
               "date": date(2022,2,2)
          },
          {
               "title": "film adı 4",
               "description": "açıklama 4",
               "imageUrl": "m4.jpg",
               "slug": "film-adi-4",
               "language": "english",
               "date": date(2022,2,15)
          }
     ],
     "sliders":[]
}
# Create your views here.

def index(request):
     movies=data["movies"]
     return render(request, 'index.html',{
          "movies": movies
     })

def movies(request):
     return render(request, 'movies.html')


def movie_details(request,slug):
     return render(request, 'movie-details.html', {"slug": slug})