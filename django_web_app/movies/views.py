from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
    #This can be simplified using the get_object_or_404
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movie':movie})
    # except Movie.DoesNotExist:
    #     raise Http404()
    # return HttpResponse(movie_id)

    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie':movie})
# Create your views here.
