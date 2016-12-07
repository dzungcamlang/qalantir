# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0002_speechmodel_voice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechmodel',
            name='voice',
            field=models.CharField(default='UK English Female', max_length=6, choices=[[0, 'UK English Female'], [1, 'UK English Male'], [2, 'US English Female'], [3, 'Arabic Male'], [4, 'Arabic Female'], [5, 'Armenian Male'], [6, 'Australian Female'], [7, 'Brazilian Portuguese Female'], [8, 'Chinese Female'], [9, 'Chinese (Hong Kong) Female'], [10, 'Chinese Taiwan Female'], [11, 'Czech Female'], [12, 'Danish Female'], [13, 'Deutsch Female'], [14, 'Dutch Female'], [15, 'Finnish Female'], [16, 'French Female'], [17, 'Greek Female'], [18, 'Hatian Creole Female'], [19, 'Hindi Female'], [20, 'Hungarian Female'], [21, 'Indonesian Female'], [22, 'Italian Female'], [23, 'Japanese Female'], [24, 'Korean Female'], [25, 'Latin Female'], [26, 'Norwegian Female'], [27, 'Polish Female'], [28, 'Portuguese Female'], [29, 'Romanian Male'], [30, 'Russian Female'], [31, 'Slovak Female'], [32, 'Spanish Female'], [33, 'Spanish Latin American Female'], [34, 'Swedish Female'], [35, 'Tamil Male'], [36, 'Thai Female'], [37, 'Turkish Female'], [38, 'Afrikaans Male'], [39, 'Albanian Male'], [40, 'Bosnian Male'], [41, 'Catalan Male'], [42, 'Croatian Male'], [43, 'Czech Male'], [44, 'Danish Male'], [45, 'Esperanto Male'], [46, 'Finnish Male'], [47, 'Greek Male'], [48, 'Hungarian Male'], [49, 'Icelandic Male'], [50, 'Latin Male'], [51, 'Latvian Male'], [52, 'Macedonian Male'], [53, 'Moldavian Male'], [54, 'Montenegrin Male'], [55, 'Norwegian Male'], [56, 'Serbian Male'], [57, 'Serbo-Croatian Male'], [58, 'Slovak Male'], [59, 'Swahili Male'], [60, 'Swedish Male'], [61, 'Vietnamese Male'], [62, 'Welsh Male'], [63, 'US English Male'], [64, 'Fallback UK Female']]),
        ),
    ]
