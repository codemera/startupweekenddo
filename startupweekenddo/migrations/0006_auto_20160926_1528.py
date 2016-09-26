# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('startupweekenddo', '0005_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.AlterField(
            model_name='event',
            name='banner_crop',
            field=image_cropping.fields.ImageRatioField('banner', '2000x1200', verbose_name='banner crop', free_crop=False, allow_fullsize=False, size_warning=False, hide_image_field=False, adapt_rotation=False, help_text=None),
        ),
    ]
