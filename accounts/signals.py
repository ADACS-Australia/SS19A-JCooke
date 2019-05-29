"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import (
    UserRoleRequest,
    UserRole,
)
from .mailer.actions import (
    email_role_change_request_to_admins,
    email_role_change_to_user,
)


@receiver(post_save, sender=UserRoleRequest, dispatch_uid='role_change_request_notify_admin')
def role_change_request_notify_admin(instance, raw=False, created=True, **kwargs):
    # Don't send the emails if:
    # * This is a raw save
    if not raw:
        # check whether we need to send the email to admins
        if created and instance.status in [UserRoleRequest.ACTION_REQUIRED, ]:
            email_role_change_request_to_admins(instance)


@receiver(pre_save, sender=UserRole, dispatch_uid='role_change_notify_user')
def role_change_notify_user(instance, raw=False, **kwargs):
    # Don't send the emails if:
    # * This is a raw save
    # * It is just created for the first time
    if not raw:

        # check whether we need to send the email to admins
        try:
            old_instance = UserRole.objects.get(id=instance.id)

            if old_instance.role != instance.role:
                email_role_change_to_user(instance, old_instance.role)
        except UserRole.DoesNotExist:
            # If there is no old instance that means it is a new entry.
            # We don't do anything for it.
            pass
