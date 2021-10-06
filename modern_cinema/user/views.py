from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


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
    # seats = request.POST.get('seats')
    # show_id = request.POST.get('show_id')
    # seats = seats[1:-1].split(',')
    # print(seats)
    # show = Show.objects.get(pk=show_id)
    # mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
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
