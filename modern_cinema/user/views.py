from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from booking.models import Booking, BookedSeat, Show


# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'user/register.html', {'user_form': user_form,
                                                  'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        next = request.POST.get('next', '')
        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST and request.POST.get('next') != '/user/login/':
                    print(request.POST)
                    return HttpResponseRedirect(request.POST.get('next'))
                else:
                    return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'user/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def booking_history(request, user_id):
    try:
        allBookings = []
        bookings = Booking.objects.filter(booked_by=user_id)
        for booking in bookings:
            bookingDetail = []
            movieDetail, seats, timeDetail = booking.id.split('|')
            movie = movieDetail.split("--", 1)
            movieName = movie[0]
            bookingDetail.append(movieName)
            bookingDetail.append(seats)
            bookingDetail.append(timeDetail)
            allBookings.append(bookingDetail)

        print(allBookings)
    #     seats = Seat.objects.filter(booked_by=user_id)
    #
    #     alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    #     numbers = [x + 1 for x in range(10)]
    #     seats_name = [x + str(y) for x in alphabets for y in numbers]
    #
    except Booking.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request, 'user/booking_history.html',
                  {'allBookings': allBookings})

    # actual_seats = Seat.objects.filter(show=show_id).order_by('id')
    #
    # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # paid_by = request.user
    # booking_id = str(show) + str(seats) + timestamp
    # book = Booking(id=booking_id, timestamp=timestamp, booked_by=paid_by)
    # book.save()
    #
    # booked_seat = []
    # for seat in seats:
    #     # Change seat to booked
    #     element = seat.replace(" ", "").replace("'", "")
    #     letter = element[0]
    #     number = element.replace(letter, "")
    #     position = ((mapping[letter] - 1) * 10) + int(number) - 1
    #     Seat.objects.filter(id=actual_seats[position].id).update(booked=1)
    #
    #     # Add seat to booked seat
    #     s = Seat.objects.get(id=actual_seats[position].id)
    #     b = Booking.objects.get(pk=booking_id)
    #     booked = BookedSeat(seat=s, booking=b)
    #     booked_seat.append(booked)
    #
    # BookedSeat.objects.bulk_create(booked_seat)
    #
    return render(request, 'user/booking_history.html')
    #               {'seats': seats,
    #                'show_info': show})
