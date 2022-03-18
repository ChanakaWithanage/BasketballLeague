from django.db import models

from coaches.models import Coach


class Team(models.Model):
    name = models.CharField(
        verbose_name='Team Name',
        max_length=100,
    )

    short_code = models.CharField(
        verbose_name='Team Code',
        max_length=10,
        null=True,
    )

    coach = models.OneToOneField(
        Coach,
        verbose_name='Coach',
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return self.name
