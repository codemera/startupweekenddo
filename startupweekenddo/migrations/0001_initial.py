# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date', null=True, blank=True)),
                ('title', models.CharField(unique=True, max_length=50)),
                ('place', models.CharField(null=True, max_length=100, blank=True)),
                ('image', models.ImageField(verbose_name='Main Image', null=True, upload_to='event/', blank=True)),
                ('registration_uri', models.URLField(verbose_name='Registration Link')),
                ('banner', image_cropping.fields.ImageCropField(verbose_name='Banner', null=True, upload_to='event/banner/', blank=True)),
                ('logo', image_cropping.fields.ImageCropField(verbose_name='Logo', null=True, upload_to='event/logo/', blank=True)),
                ('banner_crop', image_cropping.fields.ImageRatioField('banner', '800x400', help_text=None, hide_image_field=False, adapt_rotation=False, free_crop=False, size_warning=False, verbose_name='banner crop', allow_fullsize=False)),
                ('logo_crop', image_cropping.fields.ImageRatioField('logo', '400x400', help_text=None, hide_image_field=False, adapt_rotation=False, free_crop=False, size_warning=False, verbose_name='logo crop', allow_fullsize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('image', image_cropping.fields.ImageCropField(upload_to='person/')),
                ('visible', models.BooleanField(default=True)),
                ('image_crop', image_cropping.fields.ImageRatioField('image', '300x300', help_text=None, hide_image_field=False, adapt_rotation=False, free_crop=False, size_warning=False, verbose_name='image crop', allow_fullsize=False)),
            ],
            options={
                'ordering': ['event', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('event', models.OneToOneField(to='startupweekenddo.Event')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(null=True, max_length=500, blank=True)),
                ('schedule', models.ForeignKey(to='startupweekenddo.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('image', image_cropping.fields.ImageCropField(upload_to='sponsors/')),
                ('category', models.IntegerField(choices=[(1, 'Diamond'), (2, 'Platinum'), (3, 'Silver'), (4, 'Bronze'), (5, 'Media Partner')])),
                ('url', models.URLField()),
                ('image_crop', image_cropping.fields.ImageRatioField('image', '300x300', help_text=None, hide_image_field=False, adapt_rotation=False, free_crop=False, size_warning=False, verbose_name='image crop', allow_fullsize=False)),
                ('event', models.ForeignKey(to='startupweekenddo.Event')),
            ],
            options={
                'ordering': ['event', 'category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('person_ptr', models.OneToOneField(serialize=False, to='startupweekenddo.Person', primary_key=True, parent_link=True, auto_created=True)),
            ],
            bases=('startupweekenddo.person',),
        ),
        migrations.CreateModel(
            name='Facilitator',
            fields=[
                ('person_ptr', models.OneToOneField(serialize=False, to='startupweekenddo.Person', primary_key=True, parent_link=True, auto_created=True)),
                ('bio', models.TextField(max_length=500)),
                ('twitter', models.CharField(max_length=25)),
            ],
            bases=('startupweekenddo.person',),
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('person_ptr', models.OneToOneField(serialize=False, to='startupweekenddo.Person', primary_key=True, parent_link=True, auto_created=True)),
                ('bio', models.TextField(max_length=500)),
                ('position', models.CharField(max_length=500)),
            ],
            bases=('startupweekenddo.person',),
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('person_ptr', models.OneToOneField(serialize=False, to='startupweekenddo.Person', primary_key=True, parent_link=True, auto_created=True)),
                ('bio', models.TextField(max_length=500)),
                ('position', models.CharField(max_length=500)),
            ],
            bases=('startupweekenddo.person',),
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('person_ptr', models.OneToOneField(serialize=False, to='startupweekenddo.Person', primary_key=True, parent_link=True, auto_created=True)),
                ('order', models.PositiveIntegerField(verbose_name='Order')),
            ],
            bases=('startupweekenddo.person',),
        ),
        migrations.AddField(
            model_name='person',
            name='event',
            field=models.ForeignKey(to='startupweekenddo.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='sponsor',
            unique_together=set([('event', 'name')]),
        ),
    ]
