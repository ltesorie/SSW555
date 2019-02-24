from datetime import datetime
from dateutil.relativedelta import relativedelta


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
    if tbv_date > today or tbv_date == today:
        print("Error:" + str(date) + "is after current date" + str(today))
    return tbv_date < today


# User Story 03 - Alyson Randall: checks that birth date occurs before death date
def US03(birth_date, death_date):
    birth = datetime.strptime(birth_date, '%d %b %Y')
    death = datetime.strptime(death_date, '%d %b %Y')
    if death < birth:
        print(" Error - US03: Individuals's birth date ", str(birth_date), " occurs after death date ", str(death_date))
    return death > birth


# User Story 04 - Alyson Randall: checks that a couple is married before getting a divorce
def US04(marr_date, div_date):
    if marr_date and div_date != 'NA':
        marriage = datetime.strptime(marr_date, '%d %b %Y')
        divorce = datetime.strptime(div_date, '%d %b %Y')
    if divorce < marriage:
        print("Error - US04: Marriage date ", str(marriage), " occurs after divorce date ", str(divorce))
        marriage > divorce


# User Story 06 - Alyson Randall: checks that divorce date occurs before death date
def US06(death_date, divorce_date):
    if divorce_date != 'NA' and death_date != 'NA':
        divorce = datetime.strptime(divorce_date, '%d %b %Y')
        death = datetime.strptime(death_date, '%d %b %Y')
        if death < divorce:
            print("Error - US06: Divorce date", str(divorce_date), " occurs after death date ", str(death_date))
        return death > divorce


# User Story 08 - Madeline Rys: checks birth date of child to ensure it is after marriage of parents
def birth_before_marriage(birthdate, marrdate):
    birth = datetime.strptime(birthdate, '%d %b %Y')
    if marrdate != 'NA':
        marr = datetime.strptime(marrdate, '%d %b %Y')

        if birth < marr:
            print("Error - US08: child's birth date ", str(birthdate) + " is before parents' marriage date ",
                  str(marrdate))

        return birth < marr


# User Story 09 - Madeline Rys: checks birth date of child to ensure it is before death of either parent
def birth_before_death(birthdate, momdeath, daddeath):
    result = True

    birth = datetime.strptime(birthdate, '%d %b %Y')

    if momdeath == 'NA' and daddeath == 'NA':
        result = True
    elif momdeath == 'NA':
        dad = datetime.strptime(daddeath, '%d %b %Y')
        dad9months = dad - relativedelta(months=9)
        if dad9months > birth:
            print("Error - US09: child's birth date ", str(birthdate) + " is after father's death date ", str(daddeath))
            result = False
    elif daddeath == 'NA':
        mom = datetime.strptime(momdeath, '%d %b %Y')
        if mom > birth:
            result = False
            print("Error - US09: child's birth date ", str(birthdate) + " is after mother's death date ", str(momdeath))
    else:
        dad = datetime.strptime(daddeath, '%d %b %Y')
        dad9months = dad - relativedelta(months=9)
        mom = datetime.strptime(momdeath, '%d %b %Y')
        if birth < mom and birth < dad9months:
            result = False
            print("Error - US09: child's birth date ", str(birthdate) + " is after parents' death dates ",
                  str(momdeath), str(daddeath))

    return result
