"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

import uuid

from django.db import models

from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    CORE_MEMBER = 'Core Member'
    COLLABORATOR = 'Collaborator'
    PUBLIC = 'Public'
    ROLE_CHOICES = [
        (CORE_MEMBER, CORE_MEMBER),
        (COLLABORATOR, COLLABORATOR),
        (PUBLIC, PUBLIC),
    ]
    name = models.CharField(max_length=55, choices=ROLE_CHOICES, default=PUBLIC, blank=False, unique=True)

    def __str__(self):
        return u'%s' % self.name


class User(AbstractUser):
    """
    User model extending AbstractUser
    """
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    UNVERIFIED = 'Unverified'
    VERIFIED = 'Verified'
    CONFIRMED = 'Confirmed'
    DELETED = 'Deleted'
    STATUS_CHOICES = [
        (UNVERIFIED, UNVERIFIED),
        (VERIFIED, VERIFIED),
        (CONFIRMED, CONFIRMED),
        (DELETED, DELETED),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=False, default=UNVERIFIED)

    @property
    def user_role(self):
        try:
            user_role = UserRole.objects.get(user=self)
            return user_role.role.name
        except UserRole.DoesNotExist:
            return ''

    def is_admin(self):
        """
        Checks whether a user is an admin or not
        :return: True or False
        """
        return self.user_role in [Role.CORE_MEMBER]

    def is_collaborator(self):
        """
        Checks whether a user is a core member or not
        :return: True or False
        """
        return self.user_role in [Role.CORE_MEMBER, Role.COLLABORATOR]

    def display_name(self):
        """
        Builds up the display name from the user name parts
        :return: String containing full name of the user
        """
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)

    def __str__(self):
        return u'%s %s (%s)' % (self.first_name, self.last_name, self.username)

    def as_json(self):
        return dict(
            id=self.id,
            value=dict(
                username=self.username,
                first_name=self.first_name,
                last_name=self.last_name,
            ),
        )

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        try:
            UserRole.objects.get(user=self)
        except UserRole.DoesNotExist:
            try:
                UserRole.objects.create(
                    user=self,
                    role=Role.objects.get(name=Role.PUBLIC)
                )
            except Role.DoesNotExist:
                pass


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_role_user', null=False, blank=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_role_role', null=False, blank=False)

    class Meta(object):
        unique_together = (
            ('user', 'role', ),
        )


class Verification(models.Model):
    """
    Model to store information for email address verification.
    Can also be used for other verifications as well.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    information = models.CharField(max_length=1024)
    expiry = models.DateTimeField(null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return u'%s' % self.information
