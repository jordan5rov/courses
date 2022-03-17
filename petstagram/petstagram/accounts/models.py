from django.db import models
from django.contrib.auth import models as auth_models

from petstagram.accounts.managers import PetstagramUserManager

# Custom Users
'''
    1. Create model extending ...
    2. Configure this module in settings.py
    3. Create user manager
'''


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()
