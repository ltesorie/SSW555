# Laura Tesoriero
# Unittests
# test US01

import unittest
from Project03 import *
from Functions import date_before_now
from datetime import date


class TestDatesBeforeNow(unittest.TestCase):

    def test_valid_date(self):
        # valid date input
        self.assertTrue(date_before_now('4 JAN 2016'))

    def test_invalid_date(self):
        self.assertFalse(date_before_now('4 JAN 2025'))

    def test_invalid_date_today(self):
        self.assertTrue(date_before_now('27 FEB 2019'))

    def test_types(self):
        self.assertRaises(TypeError, date_before_now, datetime.today())

    def test_invalid_no_input(self):
        self.assertRaises(ValueError, date_before_now, 'NA')


class TestAge150(unittest.TestCase):

    def test_valid_date(self):
        # valid date input
        self.assertTrue(getage('4 JAN 2016'))

    def test_invalid_date(self):
        self.assertFalse(date_before_now('4 JAN 2025'))

    def test_invalid_date_today(self):
        self.assertTrue(date_before_now('27 FEB 2019'))

    def test_types(self):
        self.assertRaises(TypeError, date_before_now, datetime.today())

    def test_invalid_no_input(self):
        self.assertRaises(ValueError, date_before_now, 'NA')


#class TestChildren(unittest.TestCase):
#    def test_input_children(self):
#        self.assertTrue(children_limit('@I6000000086676587147@, @F6000000086677299999@')


class TestHUSBandWife(unittest.TestCase):
    def test_input_husb(self):
        p1 = "F"
        p2 = "M"
        f1 = "HUSB"
        f2 = "WIFE"
        f4 = "NA"

        self.assertFalse(correct_gender_role(p1, f2, f4))
        self.assertTrue(correct_gender_role(p2, f1, f4))
        self.assertFalse(correct_gender_role(p2, f4, f2))
        self.assertTrue(correct_gender_role(p1, f4, f2))
