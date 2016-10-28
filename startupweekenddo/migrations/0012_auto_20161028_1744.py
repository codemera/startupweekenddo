# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('startupweekenddo', '0011_pressrelease'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collaborator',
            options={'verbose_name': 'Colaborador', 'verbose_name_plural': 'Colaboradores'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Evento', 'ordering': ['-start_date', 'title'], 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterModelOptions(
            name='facilitator',
            options={'verbose_name': 'Facilitador', 'verbose_name_plural': 'Facilitadores'},
        ),
        migrations.AlterModelOptions(
            name='homepagedata',
            options={'verbose_name': 'Información de Homepage', 'ordering': ['-date_added', 'enabled'], 'verbose_name_plural': 'Informaciones de Homepage'},
        ),
        migrations.AlterModelOptions(
            name='judge',
            options={'verbose_name': 'Juez', 'verbose_name_plural': 'Jueces'},
        ),
        migrations.AlterModelOptions(
            name='mentor',
            options={'verbose_name': 'Mentor', 'verbose_name_plural': 'Mentores'},
        ),
        migrations.AlterModelOptions(
            name='organizer',
            options={'verbose_name': 'Organizador', 'ordering': ['event', 'order'], 'verbose_name_plural': 'Organizadore'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Persona', 'ordering': ['event', 'name'], 'verbose_name_plural': 'Gente'},
        ),
        migrations.AlterModelOptions(
            name='pressrelease',
            options={'verbose_name': 'Press Release', 'ordering': ['-date_added'], 'verbose_name_plural': 'Press Releases'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Pregunta Frecuente', 'ordering': ['category__order', 'order', 'id'], 'verbose_name_plural': 'Preguntas Frecuentes'},
        ),
        migrations.AlterModelOptions(
            name='questioncategory',
            options={'verbose_name': 'Categoria de Preguntas', 'ordering': ['order', 'id'], 'verbose_name_plural': 'Categorias de Preguntas'},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': 'Horario', 'verbose_name_plural': 'Horarios'},
        ),
        migrations.AlterModelOptions(
            name='scheduleitem',
            options={'verbose_name': 'Punto de Agenda', 'verbose_name_plural': 'Puntos de Agenda'},
        ),
        migrations.AlterModelOptions(
            name='sponsor',
            options={'verbose_name': 'Patrocinador', 'ordering': ['event', 'category', 'name'], 'verbose_name_plural': 'Patrocinadores'},
        ),
        migrations.AddField(
            model_name='event',
            name='about',
            field=mezzanine.core.fields.RichTextField(blank=True, verbose_name='Acerca de', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, verbose_name='Fecha de Finalización', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ubicación', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.PositiveIntegerField(default=0, verbose_name='Participantes'),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_uri',
            field=models.URLField(verbose_name='Link de Registro'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(verbose_name='Fecha de Comienzo'),
        ),
        migrations.AlterField(
            model_name='homepagedata',
            name='about',
            field=mezzanine.core.fields.RichTextField(verbose_name='Acerca de'),
        ),
        migrations.AlterField(
            model_name='homepagedata',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Agregado'),
        ),
        migrations.AlterField(
            model_name='homepagedata',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='Habilitado'),
        ),
        migrations.AlterField(
            model_name='homepagedata',
            name='header',
            field=mezzanine.core.fields.RichTextField(verbose_name='Encabezado'),
        ),
        migrations.AlterField(
            model_name='homepagedata',
            name='video_description',
            field=mezzanine.core.fields.RichTextField(verbose_name='Descripción de Video'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=image_cropping.fields.ImageCropField(upload_to='person/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='person',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Visible'),
        ),
        migrations.AlterField(
            model_name='pressrelease',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Agregado'),
        ),
        migrations.AlterField(
            model_name='pressrelease',
            name='press_file',
            field=models.FileField(upload_to='press_releases/', verbose_name='Archivo de Prensa'),
        ),
        migrations.AlterField(
            model_name='pressrelease',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Publicado?'),
        ),
        migrations.AlterField(
            model_name='pressrelease',
            name='title',
            field=models.CharField(unique=True, max_length=100, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=mezzanine.core.fields.RichTextField(verbose_name='Respuesta'),
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(unique=True, max_length=200, verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='questioncategory',
            name='name',
            field=models.CharField(unique=True, max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='questioncategory',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Descripción', null=True),
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='time',
            field=models.DateTimeField(verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='category',
            field=models.IntegerField(verbose_name='Category', choices=[(1, 'Diamante'), (2, 'Platino'), (3, 'Plata'), (4, 'Bronce'), (5, 'Media Partner')]),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='image',
            field=image_cropping.fields.ImageCropField(upload_to='sponsors/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]
