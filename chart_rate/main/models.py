from django.db import models
from django.contrib.auth.models import User


class RateHistory(models.Model):
    ua_rate = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, )

    class Meta:
        verbose_name_plural = 'Rates history'

    def __str__(self):
        return f'{self.ua_rate} | {self.date}'
