# Author: Madeline Rys
# CS 555 Project 03
# I pledge my honor that I have abided by the Stevens Honor System.

import datetime
import calendar
from prettytable import PrettyTable
import unittest

# class Family:
# 	def __init__(self, familyid, husbandid = "", wifeid = "", childids = [], marriagedate = "", divorcedate = "" ):
# 		self.fam_id = familyid
# 		self.husb_id = husbandid
# 		self.wife_id = wifeid
# 		self.child_ids = childids
# 		self.mar_date = marriagedate
# 		self.div_date = divorcedate

# class Individual:
# 	def __init__(self):

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

    def print_individual_table(self):
        table0 = PrettyTable()
        table0.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
        for indi in self:
            table0.add_row([self[indi].INDI, self[indi].NAME, self[indi].BIRT, self[indi].AGE, self[indi].DEAT, self[indi].FAMC, self[indi].FAMS
            ])
        print("Individuals\n", table0)

def main(file):
    ged_file = open(file, 'r')
    for line in ged_file:
        line_split = (line.rstrip()).split(' ')

        if len(line_split) > 2:
            if line_split[2] == "INDI" or line_split[2] == "FAM":
                line_ged = Gedcom(level=line_split[0], tag=line_split[2], argument=line_split[1])
                line_ged.printged(line)
            else:
                line_ged = Gedcom(level=line_split[0], tag=line_split[1], argument=' '.join(line_split[2:]))
                line_ged.printged(line)
        else:
            line_ged = Gedcom(level=line_split[0], tag=line_split[1], argument="")
            line_ged.printged(line)


filename = 'kardashian-family-tree.ged'
main(filename);