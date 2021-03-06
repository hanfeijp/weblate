# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import weblate.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0135_auto_20180518_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='add_message',
            field=models.TextField(default='Added translation using Weblate ({{ language_name }})\n\n', help_text='You can use format strings for various information, please check documentation for more details.', validators=[weblate.utils.validators.validate_render], verbose_name='Commit message when adding translation'),
        ),
        migrations.AlterField(
            model_name='component',
            name='commit_message',
            field=models.TextField(default='Translated using Weblate ({{ language_name }})\n\nCurrently translated at {{ stats.translated_percent }}% ({{ stats.translated }} of {{ stats.all }} strings)\n\nTranslation: {{ project_name }}/{{ component_name }}\nTranslate-URL: {{ url }}', help_text='You can use format strings for various information, please check documentation for more details.', validators=[weblate.utils.validators.validate_render], verbose_name='Commit message when translating'),
        ),
        migrations.AlterField(
            model_name='component',
            name='delete_message',
            field=models.TextField(default='Deleted translation using Weblate ({{ language_name }})\n\n', help_text='You can use format strings for various information, please check documentation for more details.', validators=[weblate.utils.validators.validate_render], verbose_name='Commit message when removing translation'),
        ),
    ]
