"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.db import models


class SearchColumn(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False, unique=True)
    display_name = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return '{name} [{display_name}]'.format(name=self.name, display_name=self.display_name)


class PublicSearchColumn(models.Model):
    column = models.OneToOneField(SearchColumn, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name='public_search_column')
    display_order = models.SmallIntegerField(unique=True, blank=False, null=False)

    def __str__(self):
        return '{name} [{order}]'.format(name=self.column.name, order=self.display_order)


class CollaboratorSearchColumn(models.Model):
    column = models.OneToOneField(SearchColumn, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name='collaborator_search_column')
    display_order = models.SmallIntegerField(unique=True, blank=False, null=False)

    def __str__(self):
        return '{name} [{order}]'.format(name=self.column.name, order=self.display_order)


class CoreMemberSearchColumn(models.Model):
    column = models.OneToOneField(SearchColumn, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name='core_member_search_column')
    display_order = models.SmallIntegerField(unique=True, blank=False, null=False)

    def __str__(self):
        return '{name} [{order}]'.format(name=self.column.name, order=self.display_order)
