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
)

CREATE_BASE_SUFFIX = '-create'
INDEX_BASE_SUFFIX = '-index'
DETAIL_BASE_SUFFIX = '-detail'

# person urls names
url_app_name = 'people'
person_urls_names = {
'index_url_name' : 'people' + INDEX_BASE_SUFFIX,
'create_url_name' : 'person' + CREATE_BASE_SUFFIX,
'detail_url_name' : 'person' + DETAIL_BASE_SUFFIX,
}

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

    
    '''
    TODO:
    
    get the list of fields an verbose names from the model, filtering the ones unwanted
    
        # layout_gen_list_theaders = model._meta.get_fields()
        # unwanted = set('cuil', 'birthday', 'document_type') - set(layout_gen_list_theaders)
        # for unwanted_key in unwanted: del layout_gen_list_theaders[unwanted_key]

    '''
    layout_gen_list_fields = model._meta.get_fields()
    
    layout_gen_list_theaders = model._meta.fields


    # layout_gen_list_theaders = {
    #     'Apellidos',
    #     'Nombres',
    #     'Dni',
    # }
    # THIS IS BADDDDDDDDDD JUST FOR FOOING!!!!!!!!!!!!!
    # layout_gen_list_fields = {
    #     'last_names',
    #     'first_names',
    #     'document_number',
    # }
    
    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        context['title_plus'] = self.title_plus
        context['layout_gen_header_title'] = self.layout_gen_header_title
        context['layout_gen_list_theaders'] = self.layout_gen_list_theaders
        context['create_link'] = url_app_name + ':' + person_urls_names['create_url_name']
        context['detail_link'] = url_app_name + ':' + person_urls_names['detail_url_name']
        
        # THIS IS BADDDDDDDDDD JUST FOR FOOING!!!!!!!!!!!!!
        context['layout_gen_list_fields'] = self.layout_gen_list_fields
        
        context['model_name'] = 'person'
        return context
    
class PersonDetailView(DetailView):
    model = Person
    template_name = 'people/person_detail.html'
    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
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