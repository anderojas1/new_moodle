# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150519_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')], max_length=20),
        ),
    ]
