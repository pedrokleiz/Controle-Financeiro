from django.shortcuts import render
from .models import (Deposit, Withdrawal)
from django.db.models import Sum
from website.functions import *
from decimal import Decimal
import datetime
from itertools import chain
from django.utils import timezone


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
    deposits = Deposit.objects.all().order_by("deposit_date").reverse()
    sumDeposits = deposits.aggregate(sum_deposits=Sum('deposit_value'))
    dicDepositRender = {'sumDeposits': sumDeposits, 'deposits': deposits}
    return render(request, 'deposit.html', dicDepositRender)


def deposit_result_view(request):
    date1 = request.POST['dateStart']
    date2 = request.POST['dateEnd']

    if(len(date1) > 0 and len(date2) > 0):
        deposits = Deposit.objects.filter(
            deposit_date__range=[date1, date2 + " 23:59:59"]).order_by("deposit_date").reverse()
        sumDeposits = deposits.aggregate(
            sum_deposits=Sum('deposit_value'))

        if (sumDeposits['sum_deposits'] == None):
            sumDeposits['sum_deposits'] = "Nenhum resultado encontrado, tente outra data"
        if (convertDate1(date1) > convertDate1(date2)):
            sumDeposits['sum_deposits'] = "A data de início precisa ser igual ou menor a data final"
    else:
        deposits = ""
        sumDeposits = {
            'sum_deposits': 'É necessário informar os dois campos de data'}
    dicDepositRender = {'sumDeposits': sumDeposits, 'deposits': deposits}
    return render(request, 'deposit.html', dicDepositRender)


def deposit_value_view(request):
    return render(request, 'depositValue.html')


def withdrawal_view(request):
    withdrawals = Withdrawal.objects.all().order_by("withdrawal_date").reverse()
    sumWithdrawals = Withdrawal.objects.aggregate(
        sum_withdrawals=Sum('withdrawal_value'))
    dicWithdrawalRender = {
        'sumWithdrawals': sumWithdrawals, 'withdrawals': withdrawals}
    return render(request, 'withdrawal.html', dicWithdrawalRender)


def withdrawal_result_view(request):
    date1 = request.POST['dateStart']
    date2 = request.POST['dateEnd']

    if(len(date1) > 0 and len(date2) > 0):
        withdrawals = Withdrawal.objects.filter(
            withdrawal_date__range=[date1, date2 + " 23:59:59"]).order_by("withdrawal_date").reverse()
        sumWithdrawals = withdrawals.aggregate(
            sum_withdrawals=Sum('withdrawal_value'))

        if (sumWithdrawals['sum_withdrawals'] == None):
            sumWithdrawals['sum_withdrawals'] = "Nenhum resultado encontrado, tente outra data"
        if (convertDate1(date1) > convertDate1(date2)):
            sumWithdrawals['sum_withdrawals'] = "A data de início precisa ser igual ou menor a data final"
    else:
        withdrawals = ""
        sumWithdrawals = {
            'sum_withdrawals': 'É necessário informar os dois campos de data'}
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
