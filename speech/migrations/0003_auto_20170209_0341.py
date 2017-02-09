# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0002_auto_20170209_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechmodel',
            name='voice',
            field=models.CharField(default='French Female', max_length=50, choices=[['UK English Female', 'UK English Female'], ['UK English Male', 'UK English Male'], ['US English Female', 'US English Female'], ['Arabic Male', 'Arabic Male'], ['Arabic Female', 'Arabic Female'], ['Armenian Male', 'Armenian Male'], ['Australian Female', 'Australian Female'], ['Brazilian Portuguese Female', 'Brazilian Portuguese Female'], ['Chinese Female', 'Chinese Female'], ['Chinese (Hong Kong) Female', 'Chinese (Hong Kong) Female'], ['Chinese Taiwan Female', 'Chinese Taiwan Female'], ['Czech Female', 'Czech Female'], ['Danish Female', 'Danish Female'], ['Deutsch Female', 'Deutsch Female'], ['Dutch Female', 'Dutch Female'], ['Finnish Female', 'Finnish Female'], ['French Female', 'French Female'], ['Greek Female', 'Greek Female'], ['Hatian Creole Female', 'Hatian Creole Female'], ['Hindi Female', 'Hindi Female'], ['Hungarian Female', 'Hungarian Female'], ['Indonesian Female', 'Indonesian Female'], ['Italian Female', 'Italian Female'], ['Japanese Female', 'Japanese Female'], ['Korean Female', 'Korean Female'], ['Latin Female', 'Latin Female'], ['Norwegian Female', 'Norwegian Female'], ['Polish Female', 'Polish Female'], ['Portuguese Female', 'Portuguese Female'], ['Romanian Male', 'Romanian Male'], ['Russian Female', 'Russian Female'], ['Slovak Female', 'Slovak Female'], ['Spanish Female', 'Spanish Female'], ['Spanish Latin American Female', 'Spanish Latin American Female'], ['Swedish Female', 'Swedish Female'], ['Tamil Male', 'Tamil Male'], ['Thai Female', 'Thai Female'], ['Turkish Female', 'Turkish Female'], ['Afrikaans Male', 'Afrikaans Male'], ['Albanian Male', 'Albanian Male'], ['Bosnian Male', 'Bosnian Male'], ['Catalan Male', 'Catalan Male'], ['Croatian Male', 'Croatian Male'], ['Czech Male', 'Czech Male'], ['Danish Male', 'Danish Male'], ['Esperanto Male', 'Esperanto Male'], ['Finnish Male', 'Finnish Male'], ['Greek Male', 'Greek Male'], ['Hungarian Male', 'Hungarian Male'], ['Icelandic Male', 'Icelandic Male'], ['Latin Male', 'Latin Male'], ['Latvian Male', 'Latvian Male'], ['Macedonian Male', 'Macedonian Male'], ['Moldavian Male', 'Moldavian Male'], ['Montenegrin Male', 'Montenegrin Male'], ['Norwegian Male', 'Norwegian Male'], ['Serbian Male', 'Serbian Male'], ['Serbo-Croatian Male', 'Serbo-Croatian Male'], ['Slovak Male', 'Slovak Male'], ['Swahili Male', 'Swahili Male'], ['Swedish Male', 'Swedish Male'], ['Vietnamese Male', 'Vietnamese Male'], ['Welsh Male', 'Welsh Male'], ['US English Male', 'US English Male'], ['Fallback UK Female', 'Fallback UK Female']]),
        ),
    ]
