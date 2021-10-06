from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from movie.models import Movie


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.movie) + "-" + "-" + str(self.date) + "-" + str(self.time)


class Seat(models.Model):
    id = models.IntegerField(primary_key=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    booked = models.IntegerField(default=0)

    class Meta:
        unique_together = ('id', 'show')

    def __str__(self):
        return str(self.id) + '_' + str(self.show)


# function to create seats
@receiver(post_save, sender=Show)
def create_seats(sender, instance, created, **kwargs):
    if created:
        for seat in range(80):
            instance.seat_set.create()


class Booking(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    timestamp = models.DateTimeField('%Y-%m-%d %H:%M:%S')
    booked_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)


class BookedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat', 'booking')

    def __str__(self):
        return str(self.seat) + '|' + str(self.booking)
