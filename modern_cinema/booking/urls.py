from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^seatchoice/(?P<show_id>\d+)/$', views.reserve_seat, name='reserve_seat'),
]