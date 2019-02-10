# Author: Alyson Randall
# CS 555 Project 02
# I pledge my honor that I have abided by the Stevens Honor System.

import datetime
import calendar

filename = "/home/alyson/Downloads/proj02test.ged"
file = open(filename, "r")

for line in file:
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