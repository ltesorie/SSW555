# I pledge my honor that I Have abided by the Stevens Honor System
# Alyson Randall, Laura Tesoriero, Madeline Rys
# Project 3

import datetime
import calendar
from prettytable import PrettyTable
import unittest


list_of_indis = {}
list_of_fams = {}

# CREATES A FAMILY BASED OFF OF TAGS
class Family:
    def __init__(self, familyid, husband = 'NA', wife = 'NA', childids=[], marriagedate="NA", divorcedate="NA"):
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

# CREATES AN INDIVIDUAL BASED OFF OF TAGS
class Individual:
    def __init__(self, indi, name = 'NA', gender = 'NA', birth = 'NA', age = 0, death='NA', child='NA', spouse='NA'):
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

    def get_age (self):
        if (self.DEAT == False):
            today_date = datetime.today()
            birth_date = datetime.strptime(self.BIRT, '%d %b %Y')
            self.AGE = today_date.year - birth_date.year - ((today_date.month, today_date.day) < (birth_date.month, birth_date.day))
        else:
            birth_date = datetime.strptime(self.BIRT, '%d %b %Y')
            death_date = datetime.strptime(self.DEAT, '%d %b %Y')
            self.AGE = death_date.year - birth_date.year - ((death_date.month, death_date.day) < (birth_date.month, birth_date.day))

class Gedcom:
    def __init__(self, level, tag, ged_id="", argument=""):
        self.level = level
        self.id = ged_id
        self.tag = tag
        self.argument = argument
        self.validtags = validtags = {
                        "0": ["INDI", "FAM", "HEAD", "TRLR", "NOTE"],
                        "1": ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"],
                        "2": ["DATE"]
                        }

    def is_tag_valid(self):
        if self.tag.upper() in self.validtags[self.level]:
            return True
        else:
            return False

# PRINT INDIVIDUALS TABLE
def print_individual_table(list_of_indis):
    table = PrettyTable()
    table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for indi in list_of_indis:
        table.add_row([
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
    print("Individuals\n", table)

# PRINT FAMILY TABLE
def print_family_table(list_of_fams):
    table = PrettyTable()
    table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for fam in list_of_fams:
        table.add_row([
            fam.FAM,
            fam.MARR,
            fam.DIV,
            fam.HUSB,
            fam.HNAME,
            fam.WIFE,
            fam.WNAME,
            fam.CHIL
        ])
    print("Families\n", table, "\n")

# GET LISTS OF INDIVIDUALS AND FAMILIES
def gedcom(ged_file):
    list_of_indis = []
    list_of_fams = []
    curr_fam_ind = -1
    curr_indi_ind = -1
    on_fam = False
    on_indi = False
    date_type = ''
    
    for line in ged_file:
        line_split = (line.rstrip()).split(' ')

        if len(line_split) > 2:
            if line_split[2] == "INDI":
                line_ged = Gedcom(level=line_split[0], tag=line_split[2], ged_id=line_split[1])
                tempindi = Individual(indi = line_ged.id)
                list_of_indis = list_of_indis.append(tempindi)
                curr_indi_ind = curr_indi_ind + 1;
                on_indi = True
                on_fam = False
            
            elif line_split[2] == "FAM":
                line_ged = Gedcom(level=line_split[0], tag=line_split[2], ged_id=line_split[1])
                tempindi = Family(familyid = line_ged.id)
                list_of_fams = list_of_fams.append(tempfam)
                curr_fam_ind = curr_fam_ind + 1;
                on_indi = False
                on_fam = True

            else:
                line_ged = Gedcom(level=line_split[0], tag=line_split[1], argument=' '.join(line_split[2:]))
                if line_ged.is_tag_valid():
                    if on_fam:
                        if line_ged.tag.upper() is 'DATE':
                            line_ged.tag = date_type
                        tag = line_ged.tag
                        curr_fam = list_of_fams[curr_fam_ind]
                        if tag.upper() is 'HUSB':
                            curr_fam.HUSB = line_ged.argument
                        if tag.upper() is 'WIFE':
                            curr_fam.WIFE = line_ged.argument

                    elif on_indi:
                        if line_ged.tag.upper() is 'DATE':
                            line_get.tag = date_type
                        tag = line_ged.tag
                        curr_indi = list_of_indis[curr_indi_ind]
                        curr_indi.tag = line_ged.argument     
        else:
            line_ged = Gedcom(level=line_split[0], tag=line_split[1], argument="")
            date_type = line_ged.tag

    for indi in list_of_indis:
        indi.get_age()

    for fam in list_of_fams:
        fam.get_name_by_id(list_of_indis)

    print_family_table(list_of_fams)
    print_individual_table(list_of_indis)

def main(filename):
    ged_file = open(filename, 'r')
    gedcom(ged_file)

filename = 'kardashian-family-tree.ged'
main(filename);