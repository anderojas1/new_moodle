# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apellidos',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]*$')]),
        ),
    ]
