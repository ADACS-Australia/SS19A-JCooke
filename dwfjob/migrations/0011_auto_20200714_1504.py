# Generated by Django 2.2.10 on 2020-07-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwfjob', '0010_auto_20200714_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobparameter',
            name='mary_seed_name',
            field=models.CharField(choices=[('rt', 'rt'), ('NOAO', 'NOAO'), ('lt', 'lt')], default='rt', max_length=20),
        ),
    ]