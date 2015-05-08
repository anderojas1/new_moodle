# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_persona_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
