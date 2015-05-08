# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_persona_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='slug',
        ),
    ]
