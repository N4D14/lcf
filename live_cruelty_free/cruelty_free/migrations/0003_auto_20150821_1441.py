# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruelty_free', '0002_auto_20150821_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Cruelty Free'), (2, 'Tests'), (3, 'Vegan'), (4, 'PETA'), (5, 'Mall Partner')]),
        ),
    ]
