# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cedula', models.CharField(serialize=False, max_length=30, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=40)),
                ('sexo', models.PositiveSmallIntegerField(choices=[(0, 'Masculino'), (1, 'Femenino')])),
                ('fecha_registro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderTeacher',
            fields=[
                ('persona_ptr', models.OneToOneField(to='app.Persona', serialize=False, auto_created=True, primary_key=True, parent_link=True)),
                ('institucion', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ['fecha_registro'],
            },
            bases=('app.persona',),
        ),
    ]
