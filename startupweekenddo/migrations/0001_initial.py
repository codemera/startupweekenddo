# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='pages.Page', primary_key=True, serialize=False)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, verbose_name='End Date', null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, verbose_name='Main Image', upload_to='event/', null=True)),
                ('registration_uri', models.URLField(verbose_name='Registration Link')),
                ('banner', image_cropping.fields.ImageCropField(blank=True, verbose_name='Banner', upload_to='event/banner/', null=True)),
                ('logo', image_cropping.fields.ImageCropField(blank=True, verbose_name='Logo', upload_to='event/logo/', null=True)),
                ('banner_crop', image_cropping.fields.ImageRatioField('banner', '800x400', help_text=None, free_crop=False, allow_fullsize=False, verbose_name='banner crop', adapt_rotation=False, hide_image_field=False, size_warning=False)),
                ('logo_crop', image_cropping.fields.ImageRatioField('logo', '400x400', help_text=None, free_crop=False, allow_fullsize=False, verbose_name='logo crop', adapt_rotation=False, hide_image_field=False, size_warning=False)),
            ],
            options={
                'ordering': ['-start_date', 'title'],
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', image_cropping.fields.ImageCropField(upload_to='person/')),
                ('visible', models.BooleanField(default=True)),
                ('image_crop', image_cropping.fields.ImageRatioField('image', '300x300', help_text=None, free_crop=False, allow_fullsize=False, verbose_name='image crop', adapt_rotation=False, hide_image_field=False, size_warning=False)),
            ],
            options={
                'ordering': ['event', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('event', models.OneToOneField(to='startupweekenddo.Event')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('time', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('schedule', models.ForeignKey(to='startupweekenddo.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', image_cropping.fields.ImageCropField(upload_to='sponsors/')),
                ('category', models.IntegerField(choices=[(1, 'Diamond'), (2, 'Platinum'), (3, 'Silver'), (4, 'Bronze'), (5, 'Media Partner')])),
                ('url', models.URLField()),
                ('image_crop', image_cropping.fields.ImageRatioField('image', '500x400', help_text=None, free_crop=False, allow_fullsize=False, verbose_name='image crop', adapt_rotation=False, hide_image_field=False, size_warning=False)),
                ('event', models.ForeignKey(to='startupweekenddo.Event')),
            ],
            options={
                'ordering': ['event', 'category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='startupweekenddo.Person', primary_key=True, serialize=False)),
            ],
            bases=('startupweekenddo.person',),
        ),
        migrations.CreateModel(
            name='Facilitator',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='startupweekenddo.Person', primary_key=True, serialize=False)),
                ('bio', models.TextField(max_length=500)),
                ('twitter', models.CharField(max_length=25)),
            ],
            bases=('startupweekenddo.person',),
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='startupweekenddo.Person', primary_key=True, serialize=False)),
                ('bio', models.TextField(max_length=500)),
                ('position', models.CharField(blank=True, max_length=500, null=True)),
            ],
            bases=('startupweekenddo.person',),
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='startupweekenddo.Person', primary_key=True, serialize=False)),
                ('bio', models.TextField(max_length=500)),
                ('position', models.CharField(blank=True, max_length=500, null=True)),
            ],
            bases=('startupweekenddo.person',),
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='startupweekenddo.Person', primary_key=True, serialize=False)),
                ('order', models.PositiveIntegerField(verbose_name='Order')),
            ],
            options={
                'ordering': ['event', 'order'],
            },
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
