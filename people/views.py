from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, request
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    DetailView,
)

# models import
from .models import (
    Person,
    Role,
)

CREATE_BASE_SUFFIX = '-create'
INDEX_BASE_SUFFIX = '-index'
DETAIL_BASE_SUFFIX = '-detail'

url_app_name = 'people'

# person urls names
person_urls_names = {
'index_url_name' : 'people' + INDEX_BASE_SUFFIX,
'create_url_name' : 'person' + CREATE_BASE_SUFFIX,
'detail_url_name' : 'person' + DETAIL_BASE_SUFFIX,
}

# role urls names
role_urls_names = {
'index_url_name' : 'role' + INDEX_BASE_SUFFIX,
'create_url_name' : 'role' + CREATE_BASE_SUFFIX,
'detail_url_name' : 'role' + DETAIL_BASE_SUFFIX,
}
# class BaseListView(ListView):
#     # layout variables
#     layout_gen_header_title = 'List of something'
#     title_plus = 'List illo'
#     exclude_fields = []
#     layout_gen_list_fields = model._meta.get_fields()
#     def get_context_data(self, **kwargs):
#         context = super(BaseListView, self).get_context_data(**kwargs)
#         context['title_plus'] = self.title_plus
#         context['layout_gen_header_title'] = self.layout_gen_header_title
#         context['create_link'] = url_app_name + ':' + some_urls_names['create_url_name']
#         context['detail_link'] = url_app_name + ':' + some_urls_names['detail_url_name']
#         context['layout_gen_list_fields'] = self.layout_gen_list_fields
#         context['exclude_fields'] = self.exclude_fields
#         context['model_name'] = 'no model defined'
#         return context
    
"""
-----------------------------------------------------------
PERSON VIEWS
-----------------------------------------------------------
"""

# def index(request):
#     return render(request, 'people/index.html')

class PersonListView(ListView):
    model = Person
    template_name = 'people/index.html'
    title_plus = 'Listado de personas'
    
    # layout variables
    layout_gen_header_title = 'Listado de personas or something like it'
    exclude_fields = [
        'id',
        'birthday',
        'cuil',
    ]
    
    layout_gen_list_fields = model._meta.get_fields()
    actions = {
        'detail': {
            'url': url_app_name + ':' + person_urls_names['detail_url_name'],
            'title': 'Detalle'
        },
        'create': {
            'url': url_app_name + ':' + person_urls_names['create_url_name'],
            'title': 'Crear',
        }
    }
    exclude_actions = ('detail')
    
    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        context['title_plus'] = self.title_plus
        context['layout_gen_header_title'] = self.layout_gen_header_title
        context['layout_gen_list_fields'] = self.layout_gen_list_fields
        context['exclude_fields'] = self.exclude_fields
        context['exclude_actions'] = self.exclude_actions        
        context['actions'] = self.actions
        context['model_name'] = 'person'
        return context
    
class PersonDetailView(DetailView):
    model = Person
    template_name = 'people/detail.html'
    layout_gen_header_title = 'Detail of person'
    title_plus = 'De tail'
    exclude_fields = []
    layout_gen_list_fields = model._meta.get_fields()
    layout_gen_list_fields = model._meta.get_fields()
    actions = {
        'detail': {
            'url': url_app_name + ':' + person_urls_names['detail_url_name'],
            'title': 'Detalle'
        },
        'create': {
            'url': url_app_name + ':' + person_urls_names['create_url_name'],
            'title': 'Crear',
        },
    }
    exclude_actions = ('detail')
    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['title_plus'] = self.title_plus
        context['layout_gen_header_title'] = self.layout_gen_header_title
        context['create_link'] = url_app_name + ':' + person_urls_names['create_url_name']
        context['layout_gen_list_fields'] = self.layout_gen_list_fields
        context['exclude_fields'] = self.exclude_fields
        context['exclude_actions'] = self.exclude_actions        
        context['actions'] = self.actions
        context['model_name'] = 'person'
        return context
    
class PersonCreateView(SuccessMessageMixin, CreateView):
    model = Person
    # form_class = PersonForm    
    # template_name = 'people/person_create.html'
    # success_message = "%(full_name)s fue creado exitosamente."
    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(
    #         cleaned_data,
    #         full_name=self.object.full_name,
    #     )
    
    
    
    
    
class RoleListView(ListView):
    model = Role
    template_name = 'people/index.html'
    title_plus = 'Listado de roles'
    
    # layout variables
    layout_gen_header_title = 'Listado de roles or something like it'
    exclude_fields = []
    
    layout_gen_list_fields = model._meta.get_fields()
    actions = {
        'detail': {
            'url': url_app_name + ':' + role_urls_names['detail_url_name'],
            'title': 'Detalle'
        },
        'create': {
            'url': url_app_name + ':' + role_urls_names['create_url_name'],
            'title': 'Crear',
        }
    }
    exclude_actions = ('detail', 'create')
    
    def get_context_data(self, **kwargs):
        context = super(RoleListView, self).get_context_data(**kwargs)
        context['title_plus'] = self.title_plus
        context['layout_gen_header_title'] = self.layout_gen_header_title
        context['layout_gen_list_fields'] = self.layout_gen_list_fields
        context['exclude_fields'] = self.exclude_fields
        context['exclude_actions'] = self.exclude_actions        
        context['actions'] = self.actions
        context['model_name'] = 'person'
        return context

"""
# TODO:
* Split views into several files
  http://stackoverflow.com/questions/1921771/django-split-views-py-in-several-files
"""