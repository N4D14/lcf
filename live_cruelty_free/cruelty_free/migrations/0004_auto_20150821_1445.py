# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruelty_free', '0003_auto_20150821_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='parent',
            field=models.ForeignKey(null=True, to='cruelty_free.Company'),
        ),
    ]
