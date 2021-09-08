from django.http import Http404
from django.shortcuts import render
from movie.models import Movie
from theatre.models import Show
from user.models import User
from user.models import UserProfile
from home.apps import Recommender
import datetime

import torch
from torch.utils.data import Dataset
import torch.nn as nn
import pytorch_lightning as pl
from torch.utils.data import DataLoader
import numpy as np



# Create your views here.
def movie_list(request):
    movies = Movie.objects.all().order_by('language')
    movie_list = []
    for i in range(0, len(movies)):
        movie_list.append(movies[i])

    #recommender here
    model = Recommender()

    all_movie_ids_list = Movie.objects.values_list('movie_id',flat=True) #get movie_id attributes of each Movie object
    all_movie_ids_list = list(map(int, all_movie_ids_list)) # convert string elements to int

    recommended_movie_list = []

    logged_in = False

    try:
        current_user_id = int(UserProfile.objects.filter(user=request.user).values_list('model_input_user_id',flat=True)[0]) # get logged in user_id
        logged_in = True
        # print(Movie.objects.filter(movie_id=2)) # filter Movie objects by movie_id
        # print(request.user) # print username of current logged in user
        # print(User.objects.filter(username=request.user)) # get logged in user's User objects
        # print(User.objects.values_list('username',flat=True)) # get all username in database
        # print(UserProfile.objects.values_list('model_input_user_id',flat=True)) # get all user's model_input_user_id
        # print(model.predict(userId=33152,movie_list=all_movie_ids_list)[:4])
        # print(model.predict(userId=25534,movie_list=all_movie_ids_list)[:4])
        # print(model.predict(userId=1423,movie_list=all_movie_ids_list)[:4])
        # print(model.predict(userId=3421,movie_list=all_movie_ids_list)[:4])

        recommender_output_list = model.predict(userId=current_user_id,movie_list=all_movie_ids_list)[:4]

        for movie_id_ in recommender_output_list:
            recommended_movie_list.append(Movie.objects.get(movie_id=movie_id_))

    # if user not logged in or no not user_id assigned
    except:
        pass

    #recommender ends


    context = {
        'movies': movie_list,
        'recommended_movies': recommended_movie_list,
        'logged_in': logged_in
    }

    return render(request, 'movie/movie_list.html', context)


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
