from django.db import models

from accounts.models import User


class Coach(models.Model):
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=100,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=100,
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
