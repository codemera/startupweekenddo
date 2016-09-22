# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupweekenddo', '0003_auto_20160922_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
