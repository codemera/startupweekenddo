# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupweekenddo', '0010_auto_20160929_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='PressRelease',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('press_file', models.FileField(upload_to='press_releases/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
