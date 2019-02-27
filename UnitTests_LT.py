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
        self.assertFalse(date_before_now('27 FEB 2019'))

    def test_types(self):
        self.assertRaises(TypeError, date_before_now, datetime.today())

    def test_invalid_no_input(self):
        self.assertRaises(ValueError, date_before_now, 'NA')

