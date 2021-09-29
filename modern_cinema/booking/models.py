from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie


class Booking(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    timestamp = models.DateTimeField('%Y-%m-%d %H:%M:%S')
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.movie) + "-" + "-" + str(self.date) + "-" + str(self.time)


class Seat(models.Model):
    no = models.CharField(max_length=3)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return self.no + str(self.show)


class BookedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat', 'booking')

    def __str__(self):
        return str(self.seat) + '|' + str(self.booking)
