"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import (
    Verification,
    UserRole,
    Role,
    UserRoleRequest,
)

# Registering the models for the admin interface to view.
admin.site.register(Role)
admin.site.register(Verification)


@admin.register(UserRole)
class UserRole(admin.ModelAdmin):
    list_display = ('user', 'role',)
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email', 'role__name']


@admin.register(UserRoleRequest)
class UserRoleRequest(admin.ModelAdmin):
    list_display = ('user', 'current_role', 'intended_role', 'request_time', 'status', 'approved_time', 'approved_by')
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email', 'intended_role__name',
                     'approved_by__username']


@admin.register(get_user_model())
class User(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_role')
    search_fields = ['username', 'first_name', 'last_name', 'email', ]
