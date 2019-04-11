# I pledge my honor that I Have abided by the Stevens Honor System
# Alyson Randall, Laura Tesoriero, Madeline Rys
# Project 3

from datetime import datetime
import calendar
from prettytable import PrettyTable
from Functions import *


# CREATES A FAMILY BASED OFF OF TAGS
class Family:
    def __init__(self, familyid, husband='NA', wife='NA', childids=[], marriagedate='NA', divorcedate="NA"):
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

    def get_death_by_id(self, list_of_indis):
        for indi in list_of_indis:
            if self.HUSB == indi.INDI or self.WIFE == indi.INDI:
                return indi.DEAT

    def is_spouse_dead(self, list_of_indis):
        for indi in list_of_indis:
            if self.HUSB == indi.INDI and indi.DEAT != 'NA':
                husbandDeath = indi.DEAT
                return husbandDeath
            elif self.WIFE == indi.INDI and indi.DEAT != 'NA':
                wifeDeath = indi.DEAT
                return wifeDeath


# CREATES AN INDIVIDUAL BASED OFF OF TAGS
class Individual:
    def __init__(self, indi, name='NA', gender='NA', birth='1 JAN 1970', age=0, death='NA', child='NA', spouse='NA'):
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

    def get_age(self):
        if (self.BIRT == 'NA'):
            self.AGE = 0
        elif self.BIRT == 'US03 ERROR':
            self.AGE = 0
        elif self.BIRT == 'US06 ERROR':
            self.AGE = 0
        elif self.BIRT == 'US07 Error':
            self.AGE = 0
        elif (self.DEAT == 'NA'):
            self.AGE = US27alive(self.BIRT)
        else:
            self.AGE = US27dead(self.BIRT,self.DEAT)

    def get_parents_marriage_by_id(self, list_of_fams):
        marr = ''
        if self.FAMC == 'NA':
            marr = ''

        for fam in list_of_fams:
            if fam.FAM == self.FAMC:
                marr = fam.MARR

        return marr

    def get_marriage_by_id(self, list_of_fams):
        marr = ''
        if self.FAMS == 'NA':
            marr = ''

        for fam in list_of_fams:
            if fam.FAM == self.FAMS:
                marr = fam.MARR

        return marr

    def get_parents_ages_by_id(self, list_of_fams, list_of_indis):
        mom_age = 0
        dad_age = 0
        for fam in list_of_fams:
            if fam.FAM == self.FAMC:
                for indi in list_of_indis:
                    if indi.INDI == fam.WIFE:
                        mom_age = indi.AGE
                    if indi.INDI == fam.HUSB:
                        dad_age = indi.AGE
        return [mom_age, dad_age]

    def get_parents_death_by_id(self, list_of_fams, list_of_indis):
        mom = ''
        dad = ''
        if self.FAMC == 'NA':
            mom = 'NA'
            dad = 'NA'

        for fam in list_of_fams:
            if fam.FAM == self.FAMC:
                mom = fam.get_death_by_id(list_of_indis)
                dad = fam.get_death_by_id(list_of_indis)

        return [mom, dad]


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
        try:
            if self.tag.upper() in self.validtags[self.level]:
                return True
            else:
                return False
        except:
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
    print("\nIndividuals")
    print(table)


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
    print("Families")
    print(table)


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
                if line_ged.is_tag_valid():
                    tempindi = Individual(indi=line_ged.id)
                    list_of_indis.append(tempindi)
                    curr_indi_ind = curr_indi_ind + 1;
                    on_indi = True
                    on_fam = False


            elif line_split[2] == "FAM":
                line_ged = Gedcom(level=line_split[0], tag=line_split[2], ged_id=line_split[1])
                if line_ged.is_tag_valid():
                    tempfam = Family(familyid=line_ged.id, childids=[])
                    list_of_fams.append(tempfam)
                    curr_fam_ind = curr_fam_ind + 1;
                    on_indi = False
                    on_fam = True

            else:
                line_ged = Gedcom(level=line_split[0], tag=line_split[1], argument=' '.join(line_split[2:]))
                if line_ged.is_tag_valid():
                    if on_fam:
                        if line_ged.tag.upper() == 'DATE':
                            line_ged.tag = date_type
                        tag = line_ged.tag

                        if tag.upper() == 'HUSB':
                            list_of_fams[curr_fam_ind].HUSB = line_ged.argument
                        if tag.upper() == 'WIFE':
                            list_of_fams[curr_fam_ind].WIFE = line_ged.argument
                        if tag.upper() == 'CHIL':
                            if line_ged.argument not in list_of_fams[curr_fam_ind].CHIL:
                                list_of_fams[curr_fam_ind].CHIL.append(line_ged.argument)
                        if tag.upper() == 'MARR':
                            list_of_fams[curr_fam_ind].MARR = line_ged.argument
                        if tag.upper() == 'DIV':
                            list_of_fams[curr_fam_ind].DIV = line_ged.argument



                    elif on_indi:
                        if line_ged.tag.upper() == 'DATE':
                            line_ged.tag = date_type
                            if not date_before_now(line_ged.argument):
                                line_ged.argument = "NA"
                        tag = line_ged.tag

                        if tag.upper() == 'NAME':
                            list_of_indis[curr_indi_ind].NAME = line_ged.argument
                        if tag.upper() == 'SEX':
                            list_of_indis[curr_indi_ind].SEX = line_ged.argument
                        if tag.upper() == 'BIRT':
                            list_of_indis[curr_indi_ind].BIRT = line_ged.argument
                        if tag.upper() == 'DEAT':
                            list_of_indis[curr_indi_ind].DEAT = line_ged.argument
                        if tag.upper() == 'FAMC':
                            list_of_indis[curr_indi_ind].FAMC = line_ged.argument
                        if tag.upper() == 'FAMS':
                            list_of_indis[curr_indi_ind].FAMS = line_ged.argument

        else:
            line_ged = Gedcom(level=line_split[0], tag=line_split[1], argument="")
            date_type = line_ged.tag

    for indi in list_of_indis:
        US03(indi.BIRT, indi.DEAT)
        indi.get_age()

        # check that parents are married before birth of individual
        parmar = indi.get_parents_marriage_by_id(list_of_fams)
        if parmar != '':
            birth_before_marriage(birthdate=indi.BIRT, marrdate=parmar)

        # check that parents were alive for birth of individual
        pardeaths = indi.get_parents_death_by_id(list_of_fams, list_of_indis)
        birth_before_death(birthdate=indi.BIRT, momdeath=pardeaths[0], daddeath=pardeaths[1])

        # check that individual is not married before age 14
        indimar = indi.get_marriage_by_id(list_of_fams)
        marriage_after_14(name=indi.NAME, marrdate=indimar, birthdate=indi.BIRT)

        # check that individuals parents are not too old
        par_ages = indi.get_parents_ages_by_id(list_of_fams, list_of_indis)
        parents_not_too_old(child_age=indi.AGE, mom_age=par_ages[0], dad_age=par_ages[1])

    for fam in list_of_fams:
        fam.get_name_by_id(list_of_indis, )
        US04(fam.MARR, fam.DIV)
        deaths = fam.is_spouse_dead(list_of_indis)
        US06(husband=deaths, wife=deaths, divorce_date=fam.DIV)
        fam.CHIL = order_siblings_by_age(list_of_children=fam.CHIL, list_of_indis=list_of_indis)

    US18(fam.HUSB, fam.WIFE, list_of_fams)
    correct_gender_role(indi.SEX, fam.HUSB, fam.WIFE)
    children_limit(list_of_fams)

    US29(list_of_indis)
    US36(list_of_indis)
    recent_births(list_of_indis)
    upcoming_birthdays(list_of_indis)
    US30(list_of_indis, list_of_fams)
    print("US31 - List of all those living under age 30 who are unmarried: %s" % str(list_living_single(list_of_indis)))
    US39(list_of_fams);


    # Prints out tables for individuals and families
    print_individual_table(list_of_indis)
    print_family_table(list_of_fams)




def main(filename):
    ged_file = open(filename, 'r')
    gedcom(ged_file)


filename = 'acceptancetest.ged'

main(filename);