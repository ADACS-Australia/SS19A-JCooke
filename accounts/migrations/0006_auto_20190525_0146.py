# Generated by Django 2.2.1 on 2019-05-24 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190524_0136'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userrole',
            unique_together=set(),
        ),
    ]