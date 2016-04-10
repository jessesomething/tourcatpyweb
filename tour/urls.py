from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.event_list, name='event_list'),
    url(r'^$', views.merch_list, name='merch_list'),
    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^merch/(?P<pk>\d+)/$', views.merch_detail, name='merch_detail'),
    url(r'^event/new/$', views.event_new, name='event_new'),
    url(r'^merch/new/$', views.merch_new, name='merch_new'),
]
