from django.db import models


class Coach(models.Model):
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=100,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=100,
    )

    def __str__(self):
        return self.first_name + " " + self.last_name
