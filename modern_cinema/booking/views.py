from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from booking.models import Show
# from .forms import SeatForm, BookingForm
import datetime


def reserve_seat(request, show_id):
    try:
        show_info = Show.objects.get(pk=show_id)
    except Show.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request, 'booking/reserve_seat.html',
                  {'show_info': show_info})


def booking_confirmation(request):
    if request.POST:
        seats = request.POST.get('selected_seat')
        show_id = request.POST.get('show_id')

        if len(seats) == 0:
            show_info = Show.objects.get(pk=show_id)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        show = Show.objects.get(pk=show_id)
        seats = seats.split(',')
        book_seat = []

        for each in seats:
            s = Seat(no=each, show=show)
            book_seat.append(s)
        Seat.objects.bulk_create(book_seat)

        ticket_price = '15' * len(book_seat)

        seat_str = ""
        for i in range(0, len(seats)):
            if i == len(seats) - 1:
                seat_str += seats[i]
            else:
                seat_str += seats[i] + ','

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        paid_by = request.user
        id = str(show) + str(seats) + timestamp
        book = Booking(id=id, timestamp=timestamp,
                       paid_amount=ticket_price, paid_by=paid_by)
        book.save()
        booked_seat = []

        # for seat in seats:
        #     print(seat)
        #     s = Seat.objects.get(no=seat, show=show)
        #     b = Booking.objects.get(pk=id)
        #     booked = BookedSeat(seat=s, booking=b)
        #     booked_seat.append(booked)
        #
        # BookedSeat.objects.bulk_create(booked_seat)

        return render(request, 'booking/booking_confirmation.html',
                      {'seats': seat_str,
                       'show': show, 'ticket_price': ticket_price})
    else:
        return redirect('/')
