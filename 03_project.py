# Laura Tesoriero

from datetime import datetime
from prettytable import PrettyTable


class Indi:
    def __init__(self):
        self.ID = ''
        self.NAME = ''
        self.AGE = ''
        self.SEX = ''
        self.BIRT = ''
        self.DEAT = ''
        self.FAMC = []
        self.FAMS = []

    def get_indi(self):
        person = [self.ID, self.NAME, self.AGE, self.SEX, self.BIRT, self.DEAT, self.FAMC, self.FAMS]
        return person


class Fam:
    def __init__(self):
        self.ID = ''
        self.MARR = ''
        self.HUSB = ''
        self.WIFE = ''
        self.CHIL = []
        self.DIV = ''

    def get_fam(self):
        family = [self.ID, self.MARR, self.HUSB, self.WIFE, self.CHIL, self.DIV]
        return family


# Story01

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


def date_before_now(date):
    today = datetime.date.today()
    tbv_date = reformat_date(date)
    if tbv_date > today:
        print("Error:" + date + "is after current date" + today)
    return tbv_date < today


def gedcom(file):
    with open(file) as text:
        for line in text:
            line = line.rstrip()
            piece = line.split(' ')
            level = piece[0]
            tag = piece[1]
            arguments = piece[2:]

            validtags = {0: ["INDI",
                             "FAM",
                             "HEAD",
                             "TRLR",
                             "NOTE"],
                         1: ["NAME",
                             "SEX",
                             "BIRT",
                             "DEAT",
                             "FAMC",
                             "FAMS",
                             "MARR",
                             "HUSB",
                             "WIFE",
                             "CHIL",
                             "DIV"],
                         2: ["DATE"]}
            # presets
            individual_create = False
            family_create = False
            born = False
            died = False
            married = False
            divorced = False
            temp = ''

            if level == 0 and tag == 'INDI':
                Indi()
            elif level == 0 and tag == 'FAM':
                Fam()


def print_individual(person):
    table00 = PrettyTable()
    table00.field_names = ['ID',
                           'NAME',
                           'SEX',
                           'BIRTHDAY',
                           'AGE',
                           'DEATH',
                           'FAMC',
                           'FAMS']
    for key in person:
        table00.add_row(person[key].ID,
                        person[key].NAME,
                        person[key].SEX,
                        person[key].BITH,
                        person[key].AGE,
                        person[key].DEAT,
                        person[key].FAMC,
                        person[key].FAMS)
        print(table00)


def print_family(fam):
    table01 = PrettyTable()
    table01.field_names = ['ID',
                           'MARRIED',
                           'DIVORCED',
                           'HUSBAND_ID',
                           'WIFE_ID',
                           'CHILDREN']
    for key in fam:
        table01.add_row(fam[key].ID,
                        fam[key].NAME,
                        fam[key].SEX,
                        fam[key].BITH,
                        fam[key].AGE,
                        fam[key].DEAT,
                        fam[key].FAMC,
                        fam[key].FAMS)
        print(table01)


def main():
    gedcom('kardashian-family-tree.ged')

    print_individual(person)
    print_family(family)


main()
