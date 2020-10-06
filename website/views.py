from django.shortcuts import render
from .models import (Deposit, Withdrawal)
from django.db.models import Sum


def index_view(request):
    total = Withdrawal.objects.aggregate(Sum('withdrawal_value'))
    outra = Withdrawal.objects.aggregate(total_price=Sum('withdrawal_value'))
    listIndexRender = {'depositValues': total,'outra':outra}
    return render(request, 'index.html', listIndexRender)


def deposit_view(request):
    return render(request, 'deposit.html')


def withdrawal_view(request):
    return render(request, 'withdrawal.html')


def statement_view(request):
    return render(request, 'statement.html')
