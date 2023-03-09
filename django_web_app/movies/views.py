from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    #SELECT * from movies_movie

    # Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1)

    return render(request, 'movies/index.html', {'movies':movies})
    # return HttpResponse(output)

def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/detail.html', {'movie':movie})
    # return HttpResponse(movie_id)
# Create your views here.
