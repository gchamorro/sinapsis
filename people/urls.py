from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'people'
urlpatterns = [
    url(r'^$', views.index, name='people-index'),
    # url(r'^especifica/(?P<person_id>[0-9]+)/$', views.detail, name='detail'),    
]