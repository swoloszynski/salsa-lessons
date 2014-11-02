from django.conf.urls import patterns, url

from lessons import views

urlpatterns = patterns('',
    # ex: /lessons/5/
    url(r'^(?P<practice_id>\d+)/$', views.practice_detail, name='practice_detail'),

    url(r'^instructors/$', views.instructors, name='instructors'),
    url(r'^$', views.index, name='index'),

)
