# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=250)),
                ('category', models.PositiveSmallIntegerField()),
                ('url', models.URLField()),
                ('phone', models.CharField(max_length=11)),
                ('parent', models.ForeignKey(to='cruelty_free.Company')),
            ],
        ),
    ]
