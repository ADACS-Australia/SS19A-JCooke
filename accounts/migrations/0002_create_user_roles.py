"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.db import migrations

from accounts.models import Role as Rol


def insert(apps, schema_editor):
    Role = apps.get_model('accounts', 'Role')

    initial_roles = [
        Rol.CORE_MEMBER,
        Rol.COLLABORATOR,
        Rol.PUBLIC,
    ]

    for role in initial_roles:
        Rol.objects.create(
            name=role,
        )


def revert(apps, schema_editor):
    Role = apps.get_model('accounts', 'Role')

    Role.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(code=insert, reverse_code=revert)
    ]
