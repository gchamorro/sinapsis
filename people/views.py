from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, request
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    DetailView,
)

def index(request):
    return render(request, 'people/index.html')