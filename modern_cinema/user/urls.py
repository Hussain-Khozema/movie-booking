from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^booking_history/(?P<user_id>\d+)/$', views.booking_history, name='booking_history'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout')
    ]
