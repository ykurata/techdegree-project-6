# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import json


def load_json(apps, schema_editor):
    """Read and store each mineral data."""
    Mineral = apps.get_model('minerals', 'Mineral')

    with open('minerals/minerals.json') as datafile:
        minerals = json.load(datafile)
    for mineral in minerals:
        Mineral(
            name=mineral.get('name', ''),
            image_filename=mineral.get('image filename', ''),
            image_caption=mineral.get('image caption', ''),
            category=mineral.get('category', ''),
            formula=mineral.get('formula', ''),
            strunz_classification=mineral.get('strunz classification', ''),
            color=mineral.get('color', ''),
            crystal_system=mineral.get('crystal system', ''),
            unit_cell=mineral.get('unit cell', ''),
            crystal_symmetry=mineral.get('crystal symmetry', ''),
            cleavage=mineral.get('cleavage', ''),
            mohs_scale_hardness=mineral.get('mohs scale hardness', ''),
            luster=mineral.get('luster', ''),
            streak=mineral.get('streak', ''),
            diaphaneity=mineral.get('diaphaneity', ''),
            optical_properties=mineral.get('optical properties', ''),
            refractive_index=mineral.get('refractive index', ''),
            crystal_habit=mineral.get('crystal habit', ''),
            specific_gravity=mineral.get('specific gravity', ''),
        ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_json),
    ]
