from django.shortcuts import render
from .models import (Deposit, Withdrawal)


def index_view(request):
    return render(request, 'index.html')


def deposit_view(request):
    deposits_from_bd = Deposit.objects.all()
    list_d = {'name': 'coco', 'lista': 'banana',
              'comida': 'feijao', 'tudo': deposits_from_bd}
    return render(request, 'deposit.html', list_d)


def withdrawal_view(request):
    return render(request, 'withdrawal.html')


def statement_view(request):
    return render(request, 'statement.html')
