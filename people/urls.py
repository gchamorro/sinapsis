from django.conf.urls import url, include
from django.contrib import admin
from . import views

from people.views import (
    person_urls_names,
    role_urls_names,
    PersonListView,
    PersonCreateView,
    PersonDetailView,
    PersonUpdateView,
    RoleListView,
)

app_name = 'people'
urlpatterns = [
    # ------------------------
    # person
    # ------------------------

    url(r'^$', PersonListView.as_view(), name=person_urls_names['index_url_name']),
    url(r'roles/$', RoleListView.as_view(), name=role_urls_names['index_url_name']),
    url(r'^crear/$', PersonCreateView.as_view(), name=person_urls_names['create_url_name']),
    url(r'^editar/(?P<pk>[0-9]+)/$', PersonUpdateView.as_view(), name=person_urls_names['edit_url_name']),
    url(r'^perfil/(?P<pk>[0-9]+)/$', PersonDetailView.as_view(), name=person_urls_names['detail_url_name']),
    url(r'^roles/detalle/(?P<pk>[0-9]+)/$', PersonDetailView.as_view(), name=role_urls_names['detail_url_name']),

    #url(r'^$', views.index, name='people-index'),
    # url(r'^especifica/(?P<person_id>[0-9]+)/$', views.detail, name='detail'),    
]