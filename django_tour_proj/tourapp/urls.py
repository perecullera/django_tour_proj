from django.conf.urls import patterns, include, url
from rest_framework import routers
from tourapp import views

#routers for the api rest framework
router = routers.DefaultRouter()
router.register(r'apartments', views.AptViewSet)

urlpatterns = patterns('',
                       url(r'^$',
                           views.index,
                           name='main'),
                       url(r'^(?P<apt_id>[0-9]+)/$', views.detail, name='detail'),
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
