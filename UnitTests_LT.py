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
        self.assertTrue(date_before_now('4 JAN 2016'))

    def test_invalid_date(self):
        self.assertFalse(date_before_now('4 JAN 2025'))

    def test_invalid_date_today(self):
        self.assertTrue(date_before_now('27 FEB 2019'))

    def test_types(self):
        self.assertRaises(TypeError, date_before_now, datetime.today())

    def test_invalid_no_input(self):
        self.assertRaises(ValueError, date_before_now, 'NA')


#class TestChildren(unittest.TestCase):
#   def test_input_children(self):
#        #list_of_children(,CHIL =  '2',CHIL =  '3',CHIL =  '4',CHIL =  '5',CHIL =  '6',CHIL =  '7',CHIL =  '8',
#        #                 CHIL = '9',CHIL =  '10',CHIL =  '11',CHIL =  '12',CHIL =  '13',CHIL =  '14',CHIL =  '15')
#        list_of_fams= [Individual(indi='01', age=29, birth='30 MAR 2019', death=' ',chil = '1'),
#                         Individual(indi='02', age=49, birth='1 APR 2019', death=' ',chil = '2'),
#                         Individual(indi='03', age=19, birth='16 MAR 2019', death=' ', chil = '3')]
#        self.assertFalse(children_limit(list_of_fams))

class TestHUSBandWife(unittest.TestCase):
    def test_input_husb(self):
        p1 = "F"
        p2 = "M"
        f1 = "HUSB"
        f2 = "WIFE"
        f4 = "NA"

        self.assertFalse(correct_gender_role(p1, f2, f1))
        self.assertFalse(correct_gender_role(p2, f1, f2))
        self.assertFalse(correct_gender_role(p2, f1, f2))
        self.assertFalse(correct_gender_role(p1, f1, f2))


class TestRecentBirth(unittest.TestCase):
    def test_norecentbirth(self):
        list_of_indis = [Individual(indi='01', age=29, birth='15 APR 1990', death=' '),
                         Individual(indi='02', age=49, birth='1 MAY 2018', death=' '),
                         Individual(indi='03', age=19, birth='1 JAN 2000', death=' ')]
        self.assertListEqual(recent_births(list_of_indis), [])

    def test_recentbirth(self):
        list_of_indis = [Individual(indi='01', age=29, birth='15 APR 1990', death=' '),
                         Individual(indi='02', age=49, birth='1 APR 2019', death=' '),
                         Individual(indi='03', age=19, birth='1 JAN 2000', death=' ')]
        self.assertListEqual(recent_births(list_of_indis), ['02'])

    def test_recentbirth_empty(self):
        list_of_indis = []
        self.assertListEqual(recent_births(list_of_indis), [])

    def test_recentbirth_multiple(self):
        list_of_indis = [Individual(indi='01', age=29, birth='30 MAR 2019', death=' '),
                         Individual(indi='02', age=49, birth='1 APR 2019', death=' '),
                         Individual(indi='03', age=19, birth='16 MAR 2019', death=' ')]
        self.assertListEqual(recent_births(list_of_indis), ['01','02','03'])

    def test_recentbirth_none(self):
        list_of_indis = [Individual(indi='01', age=29, birth='30 MAR 1997', death=' '),
                         Individual(indi='02', age=49, birth='1 APR 2013', death=' '),
                         Individual(indi='03', age=19, birth='16 MAR 2014', death=' ')]
        self.assertListEqual(recent_births(list_of_indis), [])

class TestUpcomingBirths(unittest.TestCase):
    def test_noupcomingbirth(self):
        list_of_indis = [Individual(indi='01', age=29, birth='15 JUN 1990', death=' '),
                         Individual(indi='02', age=49, birth='16 MAY 2018', death=' '),
                         Individual(indi='03', age=19, birth='1 JAN 2000', death=' ')]
        self.assertListEqual(upcoming_birthdays(list_of_indis), [])

    def test_upcomingbirth(self):
        list_of_indis = [Individual(indi='01', age=29, birth='15 MAY 1990', death=' '),
                         Individual(indi='02', age=49, birth='16 APR 1996', death=' '),
                         Individual(indi='03', age=19, birth='1 JAN 2000', death=' ')]
        self.assertListEqual(upcoming_birthdays(list_of_indis), ['02'])

    def test_upcomingbirth_empty(self):
        list_of_indis = []
        self.assertListEqual(upcoming_birthdays(list_of_indis), [])

    def test_upcomingbirth_multiple(self):
        list_of_indis = [Individual(indi='01', age=29, birth='29 APR 1993', death=' '),
                         Individual(indi='02', age=49, birth='13 APR 1985', death=' '),
                         Individual(indi='03', age=19, birth='1 MAY 1992', death=' ')]
        self.assertListEqual(upcoming_birthdays(list_of_indis), ['01','02','03'])

    def test_upcomingbirth_none(self):
        list_of_indis = [Individual(indi='01', age=29, birth='30 MAY 1997', death=' '),
                         Individual(indi='02', age=49, birth='1 JUN 2013', death=' '),
                         Individual(indi='03', age=19, birth='16 JUL 2014', death=' ')]
        self.assertListEqual(upcoming_birthdays(list_of_indis), [])


class TestUS27(unittest.TestCase):
    def test_age(self):
        self.assertTrue(US27dead('28 JUN 2010','27 FEB 2019'))

    def test_notdead(self):
        self.assertFalse(US27dead('28 JUN 2010', 'NA'))

    def test_age(self):
        self.assertTrue(US27alive('28 JUN 2010'))

    def test_150(self):
        self.assertFalse(US27alive('28 JUN 1850'))


class TestUS30(unittest.TestCase):
    def testEmpty(self):
        list_of_indis = []
        list_of_fams = []
        self.assertListEqual(US30(list_of_indis,list_of_fams), [])
