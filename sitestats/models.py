from django.utils import timezone
from django.db import models
from accounts.models import User


class Stat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(verbose_name='login time',
                                      default=timezone.now())
    logout_time = models.DateTimeField(verbose_name='logout time', null=True)
    login_count = 0
    total_online_time = 0
