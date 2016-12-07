# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0004_auto_20161207_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechmodel',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
