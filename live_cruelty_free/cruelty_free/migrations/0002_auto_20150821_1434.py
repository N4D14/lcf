# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruelty_free', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tests'), (2, 'Vegan'), (3, 'PETA'), (4, 'Mall Partner')]),
        ),
    ]
