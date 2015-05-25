# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150523_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterTeacher',
            fields=[
                ('persona_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='app.Persona')),
                ('anios_exp', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['anios_exp'],
            },
            bases=('app.persona',),
        ),
    ]
