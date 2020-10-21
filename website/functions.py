from decimal import Decimal
import datetime
# auxiliar methods for views.py


def makeStatement(listOfDict):
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

    newList = sorted(listOfDict, key=lambda k: k['date'])

    return newList


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


def convertDate(dateNotConverted):
    #datetime.datetime(2020, 10, 7, 18, 6, 2, 664283)
    # October 20, 2020 - 21:38:12

    listOfDates = re.split("( )", dateNotConverted)
    months = {	'January': 1,
               'February': 2,
               'March': 3,
               'April': 4,
               'May': 5,
               'June': 6,
               'July': 7,
               'August': 8,
               'September': 9,
               'October': 10,
               'November': 11,
               'December': 12}

    year = int(listOfDates[4])
    month = months[(listOfDates[0])]
    day = int(listOfDates[2][:-1])

    dateConverted = datetime.datetime(year, month, day)
    return(dateConverted)
