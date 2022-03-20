from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    Admin = 1
    Coach = 2
    Player = 3

    USER_TYPES = (
        (Admin, 'Admin'),
        (Coach, 'Coach'),
        (Player, 'Player'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=1)

