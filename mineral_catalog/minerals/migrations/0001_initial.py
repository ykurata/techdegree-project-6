# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('image_filename', models.ImageField(upload_to='', verbose_name='Uploaded image')),
                ('image_caption', models.CharField(max_length=255, blank=True)),
                ('category', models.CharField(max_length=255, blank=True)),
                ('formula', models.CharField(max_length=255, blank=True)),
                ('strunz_classification', models.CharField(max_length=255, blank=True)),
                ('color', models.CharField(max_length=255, blank=True)),
                ('crystal_system', models.CharField(max_length=255, blank=True)),
                ('unit_cell', models.CharField(max_length=255, blank=True)),
                ('crystal_symmetry', models.CharField(max_length=255, blank=True)),
                ('cleavage', models.CharField(max_length=255, blank=True)),
                ('mohs_scale_hardness', models.CharField(max_length=255, blank=True)),
                ('luster', models.CharField(max_length=255, blank=True)),
                ('streak', models.CharField(max_length=255, blank=True)),
                ('diaphaneity', models.CharField(max_length=255, blank=True)),
                ('optical_properties', models.CharField(max_length=255, blank=True)),
                ('refractive_index', models.CharField(max_length=255, blank=True)),
                ('crystal_habit', models.CharField(max_length=255, blank=True)),
                ('specific_gravity', models.CharField(max_length=255, blank=True)),
            ],
        ),
    ]
