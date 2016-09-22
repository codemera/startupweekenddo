# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupweekenddo', '0002_event_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilitator',
            name='twitter',
            field=models.CharField(null=True, max_length=25, blank=True),
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='schedule',
            field=models.ForeignKey(to='startupweekenddo.Schedule', related_name='items'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='event',
            field=models.ForeignKey(to='startupweekenddo.Event', related_name='sponsors'),
        ),
    ]
