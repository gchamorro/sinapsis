#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import (
    ModelForm,
)

from .models import (
    Person,
)

from django.forms import (
    ModelForm,
    TextInput,
    DateInput,
    Textarea,
    RadioSelect,
    Select,
    SelectMultiple,
    HiddenInput,
    ValidationError,
)

from django.forms.extras.widgets import SelectDateWidget

import re

class PersonForm(ModelForm):                    

    def clean(self):
        cleaned_data = super(PersonForm, self).clean()
        cuil = cleaned_data.get('cuil')
        document_number = cleaned_data.get('document_number')
        last_names = cleaned_data.get('last_names')
        first_names = cleaned_data.get('first_names')
        """
        last_names & first_names are saved capitalized, trimed, and letting withe-spaces on multiple names only one
        '   LASTNAME, FIrstName    anoTherName   ' is cleaned as 'Lastname, Firstname Anothername'
        """
        
        # TODO this should be a def
        # def sanitize_names(args):
        #     for name in args:
        #         if name:
        #
        
        # sanitize last_names
        if last_names:
            last_names = last_names.title() # Capitalize
            last_names = last_names.strip() # strip white spaces from start-end
            last_names = re.sub('\s+', ' ', last_names) # convert multiple whitespace into one
        # sanitize first_names            
        if first_names:
            first_names = first_names.title() # Capitalize      
            first_names = first_names.strip() # strip white spaces from start-end
            first_names = re.sub('\s+', ' ', first_names) # convert multiple whitespace into one 
        
        # if cuil is defined it can be used to save document...
        if cuil:
            extract_document_from_cuil = cuil[2:10]
            if not document_number:
                self.cleaned_data['document_number'] = extract_document_from_cuil
        # if cuil is defined compare with document match
        if document_number and cuil:            
            if extract_document_from_cuil != document_number:
                raise ValidationError('El cuil no se corresponde con el documento')
            
        return self.cleaned_data
                
    class Meta:
        model = Person
        fields = '__all__'
        exclude = [
            'photo_name',
        ]

        widgets = {
            'last_names': TextInput(attrs={'placeholder': 'Escriba todos sus apellidos'}),
            'first_names': TextInput(attrs={'placeholder': 'Escriba todos sus nombres'}),
            'document_number': TextInput(attrs={'placeholder': '8 dígitos sin espacios o puntos'}),
            'cuil': TextInput(attrs={'placeholder': '11 dígitos sin guiones, espacios o puntos'}),
            'birth_date': SelectDateWidget(years=range(1950, 2050), attrs={'class': 'datepicker', 'data-date-format': 'dd/mm/yyyy'}),
            # 'birth_date': TextInput(attrs = {'data-provide': 'datepicker', 'data-date-format': 'dd/mm/yyyy'}),
            # 'sex': RadioSelect(attrs = {}),
        }
        
        labels = {
            """
            'last_names': 'Apellidos',
            'first_names': 'Nombres',
            'document_number': 'Documento',
            'birth_date': 'Fecha de nacimiento',
            """
        }
"""
TODO:
* check homonimus
* check repeated documents (unique?)
* let extract cuil from document? If you have document you can calculate cuil!!!!! NOnonono
* calculate cuil valid
https://es.wikipedia.org/wiki/Clave_%C3%9Anica_de_Identificaci%C3%B3n_Tributaria#Procedimiento_para_obtener_el_d.C3.ADgito_verificador
  
"""

def calculate_cuil(doc):
    pass