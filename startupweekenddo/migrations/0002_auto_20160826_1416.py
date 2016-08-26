# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('startupweekenddo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizer',
            options={'ordering': ['event', 'order']},
        ),
        migrations.AlterField(
            model_name='judge',
            name='position',
            field=models.CharField(null=True, max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='position',
            field=models.CharField(null=True, max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='image_crop',
            field=image_cropping.fields.ImageRatioField('image', '500x400', free_crop=False, adapt_rotation=False, hide_image_field=False, help_text=None, allow_fullsize=False, size_warning=False, verbose_name='image crop'),
        ),
    ]
