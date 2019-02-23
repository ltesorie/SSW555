from datetime import datetime


def reformat_date(date):
    month_to_num = {'JAN': 1,
                    'FEB': 2,
                    'MAR': 3,
                    'APR': 4,
                    'MAY': 5,
                    'JUN': 6,
                    'JUL': 7,
                    'AUG': 8,
                    'SEP': 9,
                    'OCT': 10,
                    'NOV': 11,
                    'DEC': 12
                    }
    mdy = date.split(' ')
    year = mdy[2]
    month = month_to_num[mdy[1]]
    day = mdy[0]
    fixed_date = datetime.date(year, month, day)
    return fixed_date


# User Story 1 - Laura T: checks dates to make sure it has occurred
def date_before_now(date):
    date = datetime.strptime(date, '%d %b %Y')
    today = datetime.now()
    tbv_date = date
    #    tbv_date = reformat_date(date)
    if tbv_date > today:
        print("Error:" + str(date) + "is after current date" + str(today))
    return tbv_date < today


# User Story 8 - Madeline Rys: checks birth date of child to ensure it is before marriage of parents
def birth_before_marriage(birthdate, marrdate):
    birth = datetime.strptime(birthdate, '%d %b %Y')
    marr = datetime.strptime(marrdate, '%d %b %Y')

    if birth < marr:
        print("US08 Error: child's birth date ", str(birthdate) + " is before parents' marriage date ", str(marrdate))

    return birth < marr
