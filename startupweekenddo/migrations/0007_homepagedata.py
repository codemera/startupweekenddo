# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('startupweekenddo', '0006_auto_20160926_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageData',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('header', mezzanine.core.fields.RichTextField()),
                ('about', mezzanine.core.fields.RichTextField()),
                ('embed_link', models.URLField(blank=True, null=True)),
                ('video_description', mezzanine.core.fields.RichTextField()),
                ('enabled', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added', 'enabled'],
            },
        ),
    ]
