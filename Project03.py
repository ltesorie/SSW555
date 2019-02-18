# Author: Madeline Rys
# CS 555 Project 03
# I pledge my honor that I have abided by the Stevens Honor System.

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


class Gedcom:
    def __init__(self, level, tag, ged_id="", argument=""):
        self.level = level
        self.id = ged_id
        self.tag = tag
        self.argument = argument
        self.validtags = {"0": ["INDI", "FAM", "HEAD", "TRLR", "NOTE"],
                          "1": ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"],
                          "2": ["DATE"]}

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
            indi.items,
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

def main(file):
    ged_file = open(file, 'r')

    info = None

    for line in file:
        line = line.split()

        if info:
            if info.get("INDI"):
                list_of_indis[current.get("INDI")] = info
            elif info.get("FAM"):
                list_of_fams[current.get("FAM")] = info

            if tag == "INDI":
                info = {"INDI": arguments}
            else:
                info = {"FAM": arguments}
        else:
            tag = line[1].upper()
            arguments = " ".join(line[2:])

        if info.get("INDI"):
            list_of_indis[current.get("INDI")] = info
        elif info.get("FAM"):
            list_of_fams[info.get("FAM")] = info


    # ex_indi = Individual(indi=1, name='stacy', gender='f', birth='1', age='11', death='NA', child='NA', spouse='NA')
    # indi_list.append(ex_indi)
    #
    # ex_fam = Family(familyid=1, husband=ex_indi.INDI, wife=ex_indi.INDI, childids=[1], marriagedate="NA",
    #               divorcedate="NA")
    # ex_fam.get_name_by_id(indi_list)
    # fam_list.append(ex_fam)

    print_family_table(list_of_fams)
    print_individual_table(list_of_indis)


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


filename = 'kardashian-family-tree.ged'
main(filename);
