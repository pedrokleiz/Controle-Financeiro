from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def deposit_view(request):
    return render(request, 'deposit.html')


def withdrawal_view(request):
    return render(request, 'withdrawal.html')


def statement_view(request):
    return render(request, 'statement.html')
