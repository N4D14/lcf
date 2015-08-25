# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruelty_free', '0005_auto_20150821_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='product',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Personal Care'), (2, 'Household Care'), (3, 'Pet Care'), (4, 'Nutrition'), (5, 'Office Supplies')], null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=11, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
