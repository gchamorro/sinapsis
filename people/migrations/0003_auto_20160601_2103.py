# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 00:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='document_number',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('\\d\\d\\d\\d\\d\\d\\d\\d', 'El nro debe constar de ocho d\xedgitos sin espacios o puntos')], verbose_name='Nro. de Documento'),
        ),
    ]