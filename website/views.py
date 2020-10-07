from django.shortcuts import render
from .models import (Deposit, Withdrawal)
from django.db.models import Sum


def index_view(request):
    sumDeposits = Deposit.objects.aggregate(
        sum_deposits=Sum('deposit_value'))
    sumWithdrawals = Withdrawal.objects.aggregate(
        sum_withdrawals=Sum('withdrawal_value'))

    balance = sumDeposits["sum_deposits"] - \
        sumWithdrawals["sum_withdrawals"]

    dicIndexRender = {'sumDeposits': sumDeposits,
                      'sumWithdrawals': sumWithdrawals, 'balance': balance}

    return render(request, 'index.html', dicIndexRender)


def deposit_view(request):
    deposits = Deposit.objects.all()
    sumDeposits = Deposit.objects.aggregate(
        total_deposits=Sum('deposit_value'))
    dicDepositRender = {'sumDeposit': sumDeposit, 'deposits': deposits}
    return render(request, 'deposit.html', dicIndexRender)


def withdrawal_view(request):
    withdrawals = Withdrawal.objects.all()
    sumWithdrawals = Withdrawal.objects.aggregate(
        total_withdrawal=Sum('withdrawal_value'))
    dicWithdrawalRender = {
        'sumWithdrawals': sumWithdrawals, 'withdrawals': withdrawals}
    return render(request, 'withdrawal.html', dicIndexRender)


def statement_view(request):
    withdrawals = Withdrawal.objects.all()
    deposits = Deposit.objects.all()
    sumDeposits = Deposit.objects.aggregate(
        sum_deposits=Sum('deposit_value'))
    sumWithdrawals = Withdrawal.objects.aggregate(
        sum_withdrawals=Sum('withdrawal_value'))
    balance = sumDeposits["sum_deposits"] - \
        sumWithdrawals["sum_withdrawals"]
    dicStatementRender = {'withdrawals': withdrawals, 'deposits': deposits,
                          'sumDeposits': sumDeposits, 'sumWithdrawals': sumWithdrawals, 'balance': balance}
    return render(request, 'statement.html')
