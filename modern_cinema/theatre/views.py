from django.http import Http404
from django.shortcuts import render
from .models import Show
import datetime


# Create your views here.


def theatre_details(request, theatre_id):
    return
    # try:
    #     theatre_info = Theatre.objects.get(pk=theatre_id)
    #     shows = Show.objects.filter(theatre=theatre_id,
    #                                 date=datetime.date.today()).order_by('movie')
    #
    #     show_list = []
    #     show_by_movie = []
    #     movie = shows[0].movie
    #     for i in range(0, len(shows)):
    #         if movie != shows[i].movie:
    #             movie = shows[i].movie
    #             show_list.append(show_by_movie)
    #             show_by_movie = []
    #         show_by_movie.append(shows[i])
    #
    #     show_list.append(show_by_movie)
    #
    #     print(show_list)
    #
    # except Theatre.DoesNotExist:
    #     raise Http404("Page does not exist")
    # return render(request, 'theatre/theatre_details.html',
    #               {'theatre_info': theatre_info, 'show_list': show_list})
