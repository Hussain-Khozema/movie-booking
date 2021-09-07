from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie

# Create your models here.

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.movie) + "-" + str(self.date) + "-" + str(self.time)
