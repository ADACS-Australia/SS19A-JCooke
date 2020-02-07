# Generated by Django 2.2.1 on 2020-01-23 01:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwfjob', '0008_jobparameter_last_mary_run'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobparameter',
            name='image_names',
            field=models.CharField(max_length=2048, validators=[django.core.validators.RegexValidator(code='invalid_image_names', message='Must be comma separated 6 digit codes', regex='^[0-9]{6}(\\s*,\\s*[0-9]{6})*$')]),
        ),
    ]
