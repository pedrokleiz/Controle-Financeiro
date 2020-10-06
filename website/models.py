from django.db import models
import datetime


class Deposit(models.Model):
    from django.utils import timezone
    deposit_name = models.CharField(max_length=50)
    deposit_value = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2)
    deposit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.deposit_name


class Withdrawal(models.Model):
    withdrawal_name = models.CharField(max_length=50)
    withdrawal_value = models.DecimalField(
        blank=False, null=False, max_digits=20, decimal_places=2)
    withdrawal_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.withdrawal_name
