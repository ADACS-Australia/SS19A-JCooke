"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from django.test import TestCase

from ..models import User, UserRole, Role
from ..utility import get_admins


class TestGetAdmin(TestCase):
    """
    Class to test get admin
    """

    def test_get_admins_no_admin(self):
        """
        tests where no admin users in the database
        :return: Nothing
        """
        admins = get_admins()
        self.assertEquals(admins.count(), 0)

    def test_get_admins_one(self):
        """
        tests where one admin user in the database
        :return: Nothing
        """
        UserRole.objects.create(
            user=User.objects.create(
                username='admin_1',
                first_name='admin_1_f',
                last_name='admin_1_l',
                email='admin_1@localhost',
            ),
            role=Role.objects.get(
                name=Role.CORE_MEMBER,
            )
        )

        admins = get_admins()
        self.assertEquals(admins.count(), 1)

    def test_get_admins_more_than_one(self):
        """
        tests where more than admin user in the database
        :return: Nothing
        """
        UserRole.objects.create(
            user=User.objects.create(
                username='admin_1',
                first_name='admin_1_f',
                last_name='admin_1_l',
                email='admin_1@localhost',
            ),
            role=Role.objects.get(
                name=Role.CORE_MEMBER,
            )
        )
        UserRole.objects.create(
            user=User.objects.create(
                username='admin_2',
                first_name='admin_2_f',
                last_name='admin_2_l',
                email='admin_2@localhost',
            ),
            role=Role.objects.get(
                name=Role.CORE_MEMBER,
            )
        )

        # Creating a user should automatically create a role
        User.objects.create(
            username='user_1',
            first_name='user_1_f',
            last_name='user_1_l',
            email='user_1@localhost',
        ),

        admins = get_admins()
        self.assertEquals(admins.count(), 2)
