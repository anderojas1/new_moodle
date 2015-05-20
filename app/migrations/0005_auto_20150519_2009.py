# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150518_0305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historialacademico',
            options={'ordering': ['titulo']},
        ),
    ]
