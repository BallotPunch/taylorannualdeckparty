from django.conf.urls import patterns, url

from rsvp import views

urlpatterns = patterns('',
	url(r'^$', views.rsvp, name='rsvp'),
)
