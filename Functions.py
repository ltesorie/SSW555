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
    today = datetime.date.today()
    tbv_date = reformat_date(date)
    if tbv_date > today:
        print("Error:" + date + "is after current date" + today)
    return tbv_date < today
