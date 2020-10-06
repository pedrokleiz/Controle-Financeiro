from django.contrib import admin
from .models import (Deposit, Withdrawal)


class DepositAdmin(admin.ModelAdmin):
    list_display = ['deposit_name', 'deposit_value', 'deposit_date']
    search_fields = ['deposit_name', 'deposit_value', 'deposit_date']


class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ['withdrawal_name', 'withdrawal_value', 'withdrawal_date']
    search_fields = ['withdrawal_name', 'withdrawal_value', 'withdrawal_date']


admin.site.register(Deposit, DepositAdmin)
admin.site.register(Withdrawal, WithdrawalAdmin)
