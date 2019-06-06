# Generated by Django 2.2.1 on 2019-06-04 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('display_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PublicSearchColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.SmallIntegerField(unique=True)),
                ('column', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='public_search_column', to='dwfsearch.SearchColumn')),
            ],
        ),
        migrations.CreateModel(
            name='CoreMemberSearchColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.SmallIntegerField(unique=True)),
                ('column', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='core_member_search_column', to='dwfsearch.SearchColumn')),
            ],
        ),
        migrations.CreateModel(
            name='CollaboratorSearchColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.SmallIntegerField(unique=True)),
                ('column', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='collaborator_search_column', to='dwfsearch.SearchColumn')),
            ],
        ),
    ]
