# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150510_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitucionEducativa',
            fields=[
                ('codigo', models.CharField(serialize=False, max_length=10, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('sede', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=50)),
                ('zona', models.PositiveSmallIntegerField(choices=[(0, 'Urbana'), (1, 'Urbana marginal'), (2, 'Rural'), (3, 'Rural de difícil acceso')])),
                ('modalidad', models.PositiveSmallIntegerField(choices=[(0, 'Académica'), (1, 'Ténica'), (2, 'Agropecuaria'), (3, 'Comercial'), (4, 'Promoción Social'), (5, 'Finanzas'), (6, 'Administación'), (7, 'Ecología'), (8, 'Medio Ambiente'), (9, 'Industrial'), (10, 'Informática'), (11, 'Minería'), (12, 'Salud'), (13, 'Recreación'), (14, 'Turismo'), (15, 'Deporte'), (16, 'Otro')])),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='SecretariaEducacion',
            fields=[
                ('codigo', models.CharField(serialize=False, max_length=15, primary_key=True)),
                ('entidad', models.PositiveSmallIntegerField(choices=[(0, 'Municipal'), (1, 'Departamental')])),
                ('nombre', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
