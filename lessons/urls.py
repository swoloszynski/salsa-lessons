from django.conf.urls import patterns, url

from lessons import views

urlpatterns = patterns('',
    # ex: /lessons/5/
    url(r'^(?P<practice_id>\d+)/$', views.practice_detail, name='practice_detail'),

    url(r'^instructors/leads/$', views.instructors_leads, name='instructors_leads'),
    url(r'^instructors/follows/$', views.instructors_follows, name='instructors_follows'),
    url(r'^instructors/$', views.instructors, name='instructors'),
    url(r'^guestlessons/$', views.guest_lessons, name='guest_lessons'),

    url(r'^$', views.index, name='index'),

)
