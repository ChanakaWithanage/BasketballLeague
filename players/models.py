from django.db import models

from accounts.models import User


class Player(models.Model):
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=100,
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=100,
    )

    team = models.ForeignKey(
        'teams.Team', related_name='player',
        verbose_name='Team',
        on_delete=models.DO_NOTHING,
        null=True, blank=True
    )

    date_of_birth = models.DateField(
        verbose_name='Date of Birth',
    )

    height = models.PositiveSmallIntegerField(
        verbose_name='Height [cm]',
    )

    weight = models.PositiveSmallIntegerField(
        verbose_name='Weight [kg]',
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
