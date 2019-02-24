# Author: Alyson Randall
# Homework 04
# Testing US03 - Birth before death

import unittest
from Functions import US03

class test_US03(unittest.TestCase):
    def test_US03(self):
        date1 = "24 FEB 2019"
        date2 = "13 MAY 2032"
        date3 = "9 NOV 2011"
        date4 = "6 OCT 1995"


        self.assertEqual(US03(date1, date2), True)

        self.assertEqual(US03(date2, date1), False)

        self.assertEqual(US03(date3, date4), False)

        self.assertEqual(US03(date4, date3), True)

        self.assertEqual(US03(date4, date1), True)

