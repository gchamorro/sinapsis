#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
#from . import global_validators
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class BaseModel(models.Model):
    def get_fields(self):
        return [{'vname':field.verbose_name, 'name':field.name, 'value':field.value_to_string(self)} for field in self._meta.fields]
    class Meta:
        abstract = True
    

class Person(BaseModel):
    DNI = 'DN'
    LIBRETA_CIVICA = 'LC'
    LIBRETA_ENROLAMIENTO = 'LE'
    PASAPORTE = 'PA'
    UNDEFINED = 'UN'
    DOCUMENT_CHOICES = (
        (DNI, 'Documento único'),
        (LIBRETA_CIVICA, 'Libreta cívica'),
        (LIBRETA_ENROLAMIENTO, 'Libreta enrolamiento'),
        (PASAPORTE, 'Pasaporte'),
        (UNDEFINED, 'No definido'),
    )
    first_names=models.CharField(
        'Nombres',
        max_length=100,
        validators=[RegexValidator(u'^[a-zA-ZñÑüÜáéíóúÁÉÍÓÚ\'\s\.]*$', 'Sólo se permiten caracteres al fabéticos')],
    )
    last_names=models.CharField(
        'Apellidos',
        max_length=100,
        validators=[RegexValidator(u'^[a-zA-ZñÑüÜáéíóúÁÉÍÓÚ\'\s\.]*$', 'Sólo se permiten caracteres al fabéticos')],
    )
    document_type = models.CharField(
        'Tipo de documento',
        max_length=2,
        choices=DOCUMENT_CHOICES,
        default=DNI
    )
    document_number = models.CharField(
        'Nro. de Documento',
        max_length=11,
        validators=[RegexValidator('\d\d\d\d\d\d\d\d', 'El nro debe constar de ocho dígitos sin espacios o puntos')],
    )
    cuil = models.CharField(
        'Cuil',
        max_length = 11,
        blank = True,
        default = '',
        validators = [RegexValidator('\d\d\d\d\d\d\d\d', 'El nro debe constar de once dígitos sin espacios o puntos')],
    )
    birthday = models.DateField(
        'Fecha de nacimiento',
        null = True,
        blank = True,
    )    
    
    def __unicode__(self):
        return self.last_names.upper() + ', ' + self.first_names.title()
    
    def _get_full_name(self):
        return '%s, %s' % (self.last_names.upper(), self.first_names.title())
    
    def _calculate_age(self):
        today = date.today()
        age = 'no birth date defined!'
        if self.birth_date:
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    def validate_names(self, value):
        validator = [RegexValidator(u'^[a-zA-ZñÑüÜáéíóúÁÉÍÓÚ\'\s\.]*$', 'Sólo se permiten caracteres al fabéticos')],
        pass
       
    full_name = property(_get_full_name)
    age = property(_calculate_age)
    
    class Meta:
        ordering = ['last_names']
        verbose_name="Persona"
        verbose_name_plural="People"
        
class Role(BaseModel):    
    role_name = models.CharField (
        'Rol',
        max_length=100,
    )
    description = models.TextField (
        'Descripción',
        max_length = 200,
        blank = True,
    )

    def __unicode__(self):
        return self.role_name
    
    def get_absolute_url(self):
        return reverse('people:role-detail', kwargs={'pk': self.pk})
    
    
    class Meta:
        ordering = ['role_name']                
        verbose_name="Rol"