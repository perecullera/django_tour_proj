from django.conf.urls import patterns, include, url
from tourapp import views

urlpatterns = patterns('',
                       url(r'^$',
                           views.index,
                           name='main'),)
