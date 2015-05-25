# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_institucioneducativa_secretariaeducacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('codigo', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=500)),
                ('porcentaje', app.models.IntegerRangeField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_cierre', models.DateField()),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('codigo_area', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=500)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['codigo_area'],
            },
        ),
        migrations.CreateModel(
            name='Cohorte',
            fields=[
                ('numero_cohorte', models.CharField(max_length=60)),
                ('semestre', models.CharField(max_length=60)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['numero_cohorte'],
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo_curso', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=500)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['codigo_curso'],
            },
        ),
        migrations.CreateModel(
            name='HistorialAcademico',
            fields=[
                ('identificador', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('tipo', models.PositiveSmallIntegerField(choices=[(0, 'Primaria'), (1, 'Bachillerato'), (2, 'Tecnico'), (3, 'Tecnologo'), (4, 'Profesional'), (4, 'Especialización'), (5, 'Doctorado')])),
                ('institucion', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('slug', models.SlugField()),
                ('leader_teacher', models.ForeignKey(to='app.LeaderTeacher')),
            ],
            options={
                'ordering': ['identificador'],
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('estado_matricula', models.PositiveSmallIntegerField(choices=[(0, 'Matriculado'), (1, 'No Matriculado'), (2, 'En Espera de Matricula')])),
                ('nota_final_curso', models.CharField(max_length=60, default=0)),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('identificacion_curso', models.ForeignKey(to='app.Curso')),
                ('identificacion_leader_teacher', models.ForeignKey(to='app.LeaderTeacher')),
            ],
            options={
                'ordering': ['estado_matricula'],
            },
        ),
        migrations.CreateModel(
            name='Ternaria',
            fields=[
                ('identificador', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nota', app.models.FloatRangeField()),
                ('slug', models.SlugField()),
                ('actividad', models.ForeignKey(to='app.Actividad')),
                ('cohorte', models.ForeignKey(to='app.Cohorte')),
                ('leader_teacher', models.ForeignKey(to='app.LeaderTeacher')),
            ],
            options={
                'ordering': ['identificador'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('contrasena', models.CharField(max_length=15)),
                ('perfil', models.PositiveSmallIntegerField(choices=[(0, 'Perfil 0'), (1, 'Perfil 1'), (2, 'Perfil 2'), (3, 'Perfil 3')])),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['usuario'],
            },
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellidos',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z\\ ]*$')]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.CharField(max_length=30, primary_key=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')], serialize=False),
        ),
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^[0-9]*$')]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z\\ ]*$')]),
        ),
    ]
