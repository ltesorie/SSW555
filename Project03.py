# Alyson Randall, Laura Tesoriero, Madeline Rys
# Project 3

import datetime
import calendar
from prettytable import PrettyTable
import unittest

class Family:
    def __init__(self, familyid, husband, wife, childids=[], marriagedate="NA", divorcedate="NA"):
        self.FAM = familyid
        self.HUSB = husband
        self.HNAME = 'NA'
        self.WIFE = wife
        self.WNAME = 'NA'
        self.CHIL = childids
        self.MARR = marriagedate
        self.DIV = divorcedate

        def get_name_by_id(self, list_of_indis):
            for indi in list_of_indis:
                if self.HUSB == indi.INDI:
                    self.HNAME = indi.NAME
                if self.WIFE == indi.INDI:
                    self.WNAME = indi.NAME
            return self

class Individual:
    def __init__(self, indi, name, gender, birth, age, death='NA', child='NA', spouse='NA'):
        self.INDI = indi
        self.NAME = name
        self.SEX = gender
        self.BIRT = birth
        self.AGE = age
        self.DEAT = death
        self.FAMC = child
        self.FAMS = spouse
        if (self.DEAT.upper() == 'NA'):
            self.ALIV = True
        else:
            self.ALIV = False


list_of_indis = {}
list_of_fams = {}

def gedcom(file):

    def __init__(self, level, tag, ged_id="", argument=""):
        self.level = level
        self.id = ged_id
        self.tag = tag
        self.argument = argument
        self.validtags = [
            'INDI',
            'NAME',
            'SEX',
            'BIRT',
            'DEAT',
            'FAMC',
            'FAMS',
            'FAM',
            'MARR',
            'HUSB',
            'WIFE',
            'CHIL',
            'DIV',
            'DATE',
            'HEAD',
            'TRLR',
            'NOTE'
        ]

        self.validindexes = [
            '0',
            '1',
            '1',
            '1',
            '1',
            '1',
            '1',
            '0',
            '1',
            '1',
            '1',
            '1',
            '1',
            '2',
            '0',
            '0',
            '0'
        ]

    def is_tag_valid(self):
        if self.tag.upper() in self.validtags:
            if self.level == self.validindexes[self.validtags.index(self.tag.upper())]:
                return 'Y'
            else:
                return 'N'
        else:
            return 'N'

# CALCULATE AGE
def get_age (birth_date, death_date):
    if ('DEAT' == False):
        today_date = datetime.today()
        birth_date = datetime.strptime(individual['BIRT'], '%d %b %Y')
        return today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))
    else:
        birth_date = datetime.strptime(individual['BIRT'], '%d %b %Y')
        death_date = datetime.strptime(individual['DEAT'], '%d %b %Y')
        return death_date.year - birth_date.year - ((death_date.month, death_date.day) < (birth_date.month, birth_date.day))


def print_individual_table(list_of_indis):
    table0 = PrettyTable()
    table0.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for indi in list_of_indis:
        table0.add_row([
            indi.INDI,
            indi.NAME,
            indi.SEX,
            indi.BIRT,
            indi.AGE,
            indi.ALIV,
            indi.DEAT,
            indi.FAMC,
            indi.FAMS
        ])
    print("Individuals\n", table0)


def print_family_table(list_of_fams):
    table0 = PrettyTable()
    table0.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for fam in list_of_fams:
        table0.add_row([
            fam.FAM,
            fam.MARR,
            fam.DIV,
            fam.HUSB,
            fam.HNAME,
            fam.WIFE,
            fam.WNAME,
            fam.CHIL
        ])
    print("Families\n", table0, "\n")


list_of_indis = {}
list_of_fams = {}

def main(filename):
    ged_file = open(filename, 'r')
    gedcom(ged_file)


    print_family_table(list_of_fams)
    print_individual_table(list_of_indis)



filename = 'kardashian-family-tree.ged'
main(filename);