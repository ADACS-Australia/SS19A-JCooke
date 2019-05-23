"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserRoleRequest
from .mailer.actions import email_role_change_request_to_admins


@receiver(post_save, sender=UserRoleRequest, dispatch_uid='role_change_request_notify_admin')
def role_change_request_notify_admin(sender, instance, update_fields, raw=False, **kwargs):
    # Don't send the emails if:
    # * This is a raw save
    if not raw:
        # check whether we need to send the email to admins
        if instance.status in [UserRoleRequest.ACTION_REQUIRED, ]:
            email_role_change_request_to_admins(instance)
