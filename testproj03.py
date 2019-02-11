import datetime
import calendar
from prettytable import PrettyTable


f = open("01_Project_SSW_555.txt")
families = []
individuals = []
famChart = PrettyTable()
columnNames_Ind = ["ID", "Names", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
columnNames_Fam = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

for line in f:
        print("-->" + line.strip())
        line = (line.rstrip()).split(" ")

        validity = "N"

        if line[0] == "0":
            if line[1] in ["HEAD", "NOTE", "TRLR", "FAM", "INDI"]:
                validity = "Y"

        if line[0] == "1":
            if line[1] in ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"]:
                validity = "Y"

        if line[0] == "2":
            if line[1] == "DATE":
                validity = "Y"

        print("<-- " + line[0] + " | " + line[1] + " | " + validity + " | ", end = ' ')
        a = 2
        for b in (line[2:]):
            print(line[a], end = ' ')
            a = a + 1
        print()

        individuals.add_row()
        families.add_row()