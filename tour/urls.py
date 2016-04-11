from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.event_list, name='event_list'),
    url(r'^event/new/$', views.event_new, name='event_new'),
    url(r'^event/(?P<pk>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^event/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^event/(?P<pk>\d+)/delete/$', views.event_delete, name='event_delete'),
    url(r'^merch/new/$', views.merch_new, name='merch_new'),
    url(r'^merch/menu/$', views.merch_menu, name='merch_menu'),
    url(r'^merch/(?P<mk>\d+)/$', views.merch_detail, name='merch_detail'),
    url(r'^merch/(?P<mk>\d+)/edit/$', views.merch_edit, name='merch_edit'),
    url(r'^merch/sell/$', views.merch_sell, name='merch_sell'),
    url(r'^merch/(?P<mk>\d+)/delete/$', views.merch_delete, name='merch_delete'),
]
