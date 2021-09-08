from django.http import Http404
from django.shortcuts import render, redirect
from .models import *
from theatre.models import Show
from .forms import SeatForm, BookingForm
import datetime


def reserve_seat(request, show_id):
    try:
        show_info = Show.objects.get(pk=show_id)
    except Show.DoesNotExist:
        raise Http404("Page does not exist")
    form = SeatForm()
    return render(request, 'booking/reserve_seat.html',
                  {'show_info': show_info, 'form': form})