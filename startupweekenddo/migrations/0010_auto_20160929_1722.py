# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupweekenddo', '0009_auto_20160929_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['category__order', 'order', 'id']},
        ),
        migrations.AddField(
            model_name='event',
            name='youtube_video_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
