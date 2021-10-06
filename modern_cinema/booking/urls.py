from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^seatchoice/(?P<show_id>\d+)/$', views.reserve_seat, name='reserve_seat'),
    url(r'^booking_confirmation/$', views.booking_confirmation, name='booking_confirmation'),
    url(r'^booking_validation/$', views.booking_validation, name='booking_validation')
]