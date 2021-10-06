from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from booking.models import Show
from django.contrib.auth.decorators import login_required
import datetime

# from .forms import SeatForm, BookingForm
import datetime


@login_required(login_url="/user/login/")
def reserve_seat(request, show_id):
    try:
        show_info = Show.objects.get(pk=show_id)
        seats = Seat.objects.filter(show=show_id)

        alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        numbers = [x + 1 for x in range(10)]
        seats_name = [x + str(y) for x in alphabets for y in numbers]

    except Show.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request, 'booking/reserve_seat.html',
                  {'show_info': show_info, 'seats_info': seats, "seats_name": seats_name})


def booking_validation(request):
    if request.POST:
        seats = request.POST.get('selected_seat')
        show_id = request.POST.get('show_id')

        if len(seats) == 0:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        show = Show.objects.get(pk=show_id)
        seats = seats.split(',')

        return render(request, 'booking/booking_validation.html',
                      {'seats': seats,
                       'show_info': show})
    else:
        return redirect('/')


def booking_confirmation(request):
    if request.POST:
        seats = request.POST.get('seats')
        show_id = request.POST.get('show_id')
        seats = seats[1:-1].split(',')
        seats_cleaned = [seat.replace(" ", "").replace("'", "") for seat in seats]

        show = Show.objects.get(pk=show_id)
        mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
        actual_seats = Seat.objects.filter(show=show_id).order_by('id')

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        paid_by = request.user
        booking_id = str(show) + ' | ' + str(seats_cleaned) + ' | ' + timestamp
        book = Booking(id=booking_id, timestamp=timestamp, booked_by=paid_by)
        book.save()

        booked_seat = []
        for seat in seats_cleaned:
            # Change seat to booked
            letter = seat[0]
            number = seat.replace(letter, "")
            position = ((mapping[letter] - 1) * 10) + int(number) - 1
            Seat.objects.filter(id=actual_seats[position].id).update(booked=1)

            # Add seat to booked seat
            s = Seat.objects.get(id=actual_seats[position].id)
            b = Booking.objects.get(pk=booking_id)
            booked = BookedSeat(seat=s, booking=b)
            booked_seat.append(booked)

        BookedSeat.objects.bulk_create(booked_seat)

        return render(request, 'booking/booking_confirmation.html',
                      {'seats': seats_cleaned,
                       'show_info': show})
    else:
        return redirect('/')
