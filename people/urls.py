from django.conf.urls import url, include
from django.contrib import admin
from . import views

from people.views import (
    person_urls_names,
    PersonListView,
    PersonCreateView,
    PersonDetailView,
)

app_name = 'people'
urlpatterns = [
    # ------------------------
    # person
    # ------------------------
    url(r'^$', PersonListView.as_view(), name=person_urls_names['index_url_name']),
    url(r'^crear/$', PersonCreateView.as_view(), name=person_urls_names['create_url_name']),
    url(r'^perfil/(?P<pk>[0-9]+)/$', PersonDetailView.as_view(), name=person_urls_names['detail_url_name']),
    #url(r'^$', views.index, name='people-index'),
    # url(r'^especifica/(?P<person_id>[0-9]+)/$', views.detail, name='detail'),    
]