"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Verification, UserRole, Role

# Registering the models for the admin interface to view.
admin.site.register(Role)
admin.site.register(Verification)


@admin.register(UserRole)
class UserRole(admin.ModelAdmin):
    list_display = ('user', 'role',)
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email', 'role__name']


@admin.register(get_user_model())
class User(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_role')
    search_fields = ['username', 'first_name', 'last_name', 'email', ]
