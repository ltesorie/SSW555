# Author: Alyson Randall
# CS 555 Project 02
# I pledge my honor that I have abided by the Stevens Honor System.

import datetime
import calendar

filename = "/home/alyson/Downloads/proj02test.ged"
file = open(filename, "r")

for line in file:
        print("-->" + line)
        line = (line.rstrip()).split(" ")

        validity = "N"

        if line[0] == "0":
            if line[1] == "HEAD" or "NOTE" or "TRLR" or "FAM" or "INDI":
                validity = "Y"


        if line[0] == "1":
            if line[1] == "NAME" or "SEX" or "BIRT" or "DEAT" or "FAMC" or "FAMS" or "MARR" or "HUSB" or "WIFE" or "CHIL" or "DIV":
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
