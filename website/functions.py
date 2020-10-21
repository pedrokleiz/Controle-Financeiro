from decimal import Decimal
import datetime
import re
# auxiliar methods for views.py


def orderListOfDicts(listOfDict):
    for dicts in listOfDict:
        for valuesOfDicts in dicts.copy():
            if(valuesOfDicts == 'withdrawal_name'):
                dicts['name'] = dicts['withdrawal_name']
                del dicts['withdrawal_name']
                dicts.update({'withdrawal_value': (
                    dicts['withdrawal_value']*(-1))})
                dicts['typeOfEntry'] = 0

            if(valuesOfDicts == 'deposit_name'):
                dicts['name'] = dicts['deposit_name']
                del dicts['deposit_name']
                dicts['typeOfEntry'] = 1

            if(valuesOfDicts == 'withdrawal_value'):
                dicts['value'] = dicts['withdrawal_value']
                del dicts['withdrawal_value']

            if(valuesOfDicts == 'deposit_value'):
                dicts['value'] = dicts['deposit_value']
                del dicts['deposit_value']

            if(valuesOfDicts == 'withdrawal_date'):
                dicts['date'] = dicts['withdrawal_date']
                del dicts['withdrawal_date']

            if(valuesOfDicts == 'deposit_date'):
                dicts['date'] = dicts['deposit_date']
                del dicts['deposit_date']

    newList = sorted(listOfDict, key=lambda k: k['date'], reverse=True)

    return newList


def convertDate1(dateNotConverted):
    # datetime.datetime(2020, 10, 7, 18, 6, 2, 664283) <- we want
    # October 20, 2020 - 21:38:12 <- we have

    listOfDates = re.split("-", dateNotConverted)

    year = int(listOfDates[0])
    month = int(listOfDates[1])
    day = int(listOfDates[2])

    dateConverted = datetime.datetime(year, month, day)
    return(dateConverted)


def convertDate2(dateNotConverted):
    # datetime.datetime(2020, 10, 7, 18, 6, 2, 664283) <- we want
    # October 20, 2020 - 21:38:12 <- we have

    listOfDates = re.split("-", dateNotConverted)

    year = int(listOfDates[0])
    month = int(listOfDates[1])
    day = int(listOfDates[2])

    dateConverted = datetime.datetime(year, month, day, 23, 59, 59)
    return(dateConverted)


def compareDates(listOfDict, date1, date2):
    datesInRange = []
    for dicts in listOfDict:
        if((dicts['date'] >= date1) and (dicts['date'] <= date2)):
            datesInRange.append(dicts)
    return datesInRange


def totalStatement(listOfDict):
    totalP = 0
    totalN = 0
    for dicts in listOfDict:
        if(dicts['value'] > 0):
            totalP = totalP + dicts['value']
        if(dicts['value'] < 0):
            totalN = totalN + dicts['value']
    return totalP+totalN
