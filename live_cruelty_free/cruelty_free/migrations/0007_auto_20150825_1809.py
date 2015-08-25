# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruelty_free', '0006_auto_20150825_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Cruelty Free'), (2, 'Tests'), (3, 'Vegan'), (4, 'PETA'), (5, 'Mall Partner'), (6, 'Vegan & PETA'), (7, 'Vegan & Mall Partner')]),
        ),
    ]
