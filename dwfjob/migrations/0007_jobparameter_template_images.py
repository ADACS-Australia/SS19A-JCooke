# Generated by Django 2.2.1 on 2019-11-29 13:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwfjob', '0006_auto_20191128_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobparameter',
            name='template_images',
            field=models.CharField(blank=True, max_length=2048, null=True, validators=[django.core.validators.RegexValidator(code='invalid_template_images', message='Must be comma separated 6 digit codes', regex='^[0-9]{6}(\\s*,\\s*[0-9]{6})*$')]),
        ),
    ]
