# Generated by Django 2.2.10 on 2020-07-14 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwfjob', '0009_auto_20200123_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobparameter',
            name='filter',
            field=models.CharField(choices=[('u', 'u Band'), ('g', 'g Band'), ('r', 'r Band'), ('i', 'i Band'), ('z', 'z Band'), ('Y', 'Y Band')], default='g Band', max_length=20),
        ),
    ]
