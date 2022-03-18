from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    USER_TYPES = (
        (1, 'Admin'),
        (2, 'Coach'),
        (3, 'Player'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=1)

