# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechmodel',
            name='voice',
            field=models.CharField(default='French Female', max_length=50),
        ),
    ]
