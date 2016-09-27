# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupweekenddo', '0007_homepagedata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagedata',
            name='embed_link',
        ),
        migrations.AddField(
            model_name='homepagedata',
            name='embed_link_id',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]
