# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupweekenddo', '0012_auto_20161028_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='category',
            field=models.IntegerField(verbose_name='Category', choices=[(1, 'Diamante'), (2, 'Platino'), (0, 'Gold'), (3, 'Plata'), (4, 'Bronce'), (5, 'Media Partner')]),
        ),
    ]
