# Author: Alyson Randall
# CS 555 Project 03
# I pledge my honor that I have abided by the Stevens Honor System.

import datetime
import calendar
from prettytable import PrettyTable

class Gedcom:
    def __init__(self, level, tag, ged_id = "", argument = ""):
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
        'FAMS'
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
	    print('<-- %s | %s | %s | %s \n' % (self.level, self.tag, self.is_tag_valid(), self.argument) )

indiList = []
famList = []

def print_individual_table():
    table0 = PrettyTable()
    table0.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for indi in indiList:
        table0.add_row([])
    print("Individuals\n", table0)

def print_family_table():
    table1 = PrettyTable()
    table1.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for fam in famList:
        table1.add_row([])
    print("Families\n", table1)


def calculate_age(birth, death):
    return death.year - birth.year - ((death.month, death.day) < (birth.month, birth.day))


def main(file):
    ged_file = open(file, 'r')
    for line in ged_file:
        line_split = (line.rstrip()).split(' ')
        if len(line_split) > 2:
        	if( line_split[2] == "INDI" or line_split[2] == "FAM" ):
        		line_ged = Gedcom(level = line_split[0], tag = line_split[2], argument = line_split[1])
        		line_ged.printged(line)
        	else:
        		line_ged = Gedcom(level = line_split[0], tag = line_split[1], argument = ' '.join(line_split[2:]))
        		line_ged.printged(line)
        else:
        	line_ged = Gedcom(level = line_split[0], tag = line_split[1], argument = "")
        	line_ged.printged(line)


print_individual_table()
print_family_table()


filename = "/home/alyson/Downloads/proj02test.ged"
main(filename);








