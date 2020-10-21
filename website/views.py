from django.shortcuts import render
from .models import (Deposit, Withdrawal)
from django.db.models import Sum
from website.functions import *
from decimal import Decimal
import datetime
from itertools import chain


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
        sum_deposits=Sum('deposit_value'))
    dicDepositRender = {'sumDeposits': sumDeposits, 'deposits': deposits}
    return render(request, 'deposit.html', dicDepositRender)


def deposit_value_view(request):
    return render(request, 'depositValue.html')


def withdrawal_view(request):
    withdrawals = Withdrawal.objects.all()
    sumWithdrawals = Withdrawal.objects.aggregate(
        sum_withdrawals=Sum('withdrawal_value'))
    dicWithdrawalRender = {
        'sumWithdrawals': sumWithdrawals, 'withdrawals': withdrawals}
    return render(request, 'withdrawal.html', dicWithdrawalRender)


def withdrawal_value_view(request):
    return render(request, 'withdrawalValue.html')


def elements_view(request):
    return render(request, 'elements.html')


def deposit_success_view(request):
    Deposit.objects.create(
        deposit_name=request.POST['description'], deposit_value=request.POST['value'])
    return render(request, 'depositSuccess.html')


def withdrawal_success_view(request):
    Withdrawal.objects.create(
        withdrawal_name=request.POST['description'], withdrawal_value=request.POST['value'])
    return render(request, 'withdrawalSuccess.html')


def statement_view(request):

    withdrawalsValue = Withdrawal.objects.values()
    depositsValue = Deposit.objects.values()

    listOfDictUnordered = list(chain(withdrawalsValue, depositsValue))

    listOfDictOrdered = orderListOfDicts(listOfDictUnordered)

    balance = totalStatement(listOfDictOrdered)

    dicStatementRender = {
        'listOfDictOrdered': listOfDictOrdered, 'balance': balance}
    return render(request, 'statement.html', dicStatementRender)


def statement_result_view(request):
    withdrawalsValue = Withdrawal.objects.values()
    depositsValue = Deposit.objects.values()

    listOfDictUnordered = list(chain(withdrawalsValue, depositsValue))
    listOfDictOrdered = orderListOfDicts(listOfDictUnordered)

    date1 = request.POST['dateStart']
    date2 = request.POST['dateEnd']

    dateConverted1 = convertDate1(date1)
    dateConverted2 = convertDate2(date2)
    listOfDictsInRange = compareDates(
        listOfDictOrdered, dateConverted1, dateConverted2)
    balance = totalStatement(listOfDictsInRange)

    if (balance == 0):
        balance = "Nenhum resultado encontrado, tente outra data"
        if (dateConverted1 > dateConverted2):
            balance = "A data de início precisa ser igual ou menor a data final"
    dicStatementRender = {
        'listOfDictOrdered': listOfDictsInRange, 'balance': balance}
    return render(request, 'statement.html', dicStatementRender)
