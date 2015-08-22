# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruelty_free', '0004_auto_20150821_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='parent',
            field=models.ForeignKey(to='cruelty_free.Company', null=True, blank=True),
        ),
    ]
