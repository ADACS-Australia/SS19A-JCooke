"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

from accounts.models import Role, User, UserRole


class TestData(object):

    public_users = []
    core_members = []
    collaborators = []

    public_users_usernames = [
        'public_user_1',
        'public_user_2',
        'public_user_3',
    ]

    core_members_usernames = [
        'core_member_1',
        'core_member_2',
        'core_member_3',
    ]

    collaborators_usernames = [
        'collaborator_1',
        'collaborator_2',
        'collaborator_3',
    ]

    def create_public_users(self):
        if self.public_users:
            return

        role = Role.objects.get(name=Role.PUBLIC)

        for username in self.public_users_usernames:
            user = User.objects.create(
                username=username,
                first_name='{} First Name'.format(username),
                last_name='{} Last Name'.format(username),
                email='{}@localhost'.format(username),
            )
            UserRole.objects.update_or_create(
                user=user,
                defaults={
                    'role': role,
                }
            )

            self.public_users.append(user)

    def create_collaborators(self):
        if self.collaborators:
            return

        role = Role.objects.get(name=Role.COLLABORATOR)

        for username in self.collaborators_usernames:
            user = User.objects.create(
                username=username,
                first_name='{} First Name'.format(username),
                last_name='{} Last Name'.format(username),
                email='{}@localhost'.format(username),
            )
            UserRole.objects.update_or_create(
                user=user,
                defaults={
                    'role': role,
                }
            )

            self.collaborators.append(user)

    def create_core_members(self):
        if self.core_members:
            return

        role = Role.objects.get(name=Role.CORE_MEMBER)

        for username in self.core_members_usernames:
            user = User.objects.create(
                username=username,
                first_name='{} First Name'.format(username),
                last_name='{} Last Name'.format(username),
                email='{}@localhost'.format(username),
            )
            UserRole.objects.update_or_create(
                user=user,
                defaults={
                    'role': role,
                }
            )

            self.core_members.append(user)
