from django.contrib.auth.models import User, Group


class AppAccount:

    def __init__(self):
        pass

    def create_new_account(self, attrs):
        user = self.create_user(attrs.get("user"))
        group = self.create_group(attrs.get("group"))
        user.groups.add(group)

        return {
            "user": user,
            "group": group
        }

    # private

    def create_group(self, attrs):
        group_name = attrs.get("name")
        group = Group.objects.create(name=group_name)
        return group

    def create_user(self, attrs):
        return User.objects.create_user(
            username=attrs.get("username"),
            email=attrs.get("email"),
            password=attrs.get("password")
        )
