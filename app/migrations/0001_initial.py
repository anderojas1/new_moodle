# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cedula', models.CharField(primary_key=True, serialize=False, max_length=30, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9, 15}$')])),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.PositiveSmallIntegerField(choices=[(0, 'Masculino'), (1, 'Femenino')])),
                ('email', models.EmailField(max_length=50)),
                ('celular', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\+?\\?\\d{9, 10}$')])),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderTeacher',
            fields=[
                ('persona_ptr', models.OneToOneField(primary_key=True, to='app.Persona', parent_link=True, serialize=False, auto_created=True)),
                ('institucion', models.CharField(max_length=60)),
                ('nivel_estudio', models.PositiveSmallIntegerField(choices=[(0, 'Bachillerato'), (1, 'Licenciatura'), (2, 'Especialización'), (3, 'Maestría'), (4, 'Doctorado')])),
            ],
            options={
                'ordering': ['fecha_registro'],
            },
            bases=('app.persona',),
        ),
    ]
