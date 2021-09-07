from django.http import Http404
from django.shortcuts import render
from movie.models import Movie
from theatre.models import Show
import datetime


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all().order_by('language')
    movie_list = []
    for i in range(0, len(movies)):
        movie_list.append(movies[i])
    return render(request, 'movie/movie_list.html', {'movies': movie_list})


def movie_details(request, movie_id):
    try:
        movie_info = Movie.objects.get(pk=movie_id)
        print(movie_info.id)
        shows = Show.objects.filter(movie=movie_id)
        show_list = []
        for i in range(0, len(shows)):
            print(shows[i])
            show_list.append(shows[i])

    except Movie.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request, 'movie/movie_details.html',
                  {'movie_info': movie_info, 'show_list': show_list})
