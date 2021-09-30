from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from booking.models import Show
from django.contrib.auth.decorators import login_required

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


def booking_confirmation(request):
    if request.POST:
        seats = request.POST.get('selected_seat')
        show_id = request.POST.get('show_id')

        if len(seats) == 0:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        show = Show.objects.get(pk=show_id)
        seats = seats.split(',')

        mapping = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
        actual_seats = Seat.objects.filter(show=show_id).order_by('id')

        for seat in seats:
            letter = seat.strip()[0]
            position = ((mapping[letter]-1) * 10) + int(seat.strip()[1]) - 1
            Seat.objects.filter(id=actual_seats[position].id).update(booked=1)
        #
        # ticket_price = '15' * len(book_seat)
        #
        # seat_str = ""
        # for i in range(0, len(seats)):
        #     if i == len(seats) - 1:
        #         seat_str += seats[i]
        #     else:
        #         seat_str += seats[i] + ','
        #
        # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # paid_by = request.user
        # id = str(show) + str(seats) + timestamp
        # book = Booking(id=id, timestamp=timestamp,
        #                paid_amount=ticket_price, paid_by=paid_by)
        # book.save()
        # booked_seat = []
        #
        # # for seat in seats:
        # #     print(seat)
        # #     s = Seat.objects.get(no=seat, show=show)
        # #     b = Booking.objects.get(pk=id)
        # #     booked = BookedSeat(seat=s, booking=b)
        # #     booked_seat.append(booked)
        # #
        # # BookedSeat.objects.bulk_create(booked_seat)
        #
        return render(request, 'booking/booking_confirmation.html',
                      {'seats': seats,
                       'show_info': show})
    else:
        return redirect('/')
