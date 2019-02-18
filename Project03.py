# Author: Madeline Rys
# CS 555 Project 03
# I pledge my honor that I have abided by the Stevens Honor System.

import datetime
import calendar
from prettytable import PrettyTable
import unittest


class Family:
    def __init__(self, familyid, husbandid="NA", wifeid="NA", childids=[], marriagedate="NA", divorcedate="NA"):
        self.FAM = familyid
        self.HUSB = husbandid
        self.WIFE = wifeid
        self.CHIL = childids
        self.MARR = marriagedate
        self.DIV = divorcedate

    def print_family_table(list_of_fams):
        table0 = PrettyTable()
        table0.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name",
                              "Children"]
        for fam in list_of_fams:
            table0.add_row([
                list_of_fams[fam].FAM,
                list_of_fams[fam].MARR,
                list_of_fams[fam].DIV,
                list_of_fams[fam].HUSB,
                'Carl',
                list_of_fams[fam].WIFE,
                'Stacy',
                list_of_fams[fam].CHIL
            ])
        print("Families\n", table0)


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

class Gedcom:
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

    def printged(self, gedcom_line):
        print('--> %s' % gedcom_line)
        print('<-- %s | %s | %s | %s \n' % (self.level, self.tag, self.is_tag_valid(), self.argument))


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
    print("Individuals\n")
    print(table0)

def main(file):
    ged_file = open(file, 'r')
    indi_list = []
    fam_list = []

    ex_indi = Individual(indi=1, name='stacy', gender='f', birth='1', age='11', death='NA', child='NA', spouse='NA')
    indi_list.append(ex_indi)

    print_individual_table(indi_list)


# for line in ged_file:
#     line_split = (line.rstrip()).split(' ')

#     if len(line_split) > 2:
#         if line_split[2] == "INDI" or line_split[2] == "FAM":
#             line_ged = Gedcom(level=line_split[0], tag=line_split[2], argument=line_split[1])
#             line_ged.printged(line)
#         else:
#             line_ged = Gedcom(level=line_split[0], tag=line_split[1], argument=' '.join(line_split[2:]))
#             line_ged.printged(line)
#     else:
#         line_ged = Gedcom(level=line_split[0], tag=line_split[1], argument="")
#         line_ged.printged(line)


filename = 'proj02test.ged'
main(filename);
