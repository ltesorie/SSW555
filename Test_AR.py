# Author: Alyson Randall
# User Story Tests

import unittest
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from Functions import US03, US04, US06, US18, US29, US36, US39
from Project03 import *


# class test(unittest.TestCase):
#     def test_US03(self):
#         print("**************TESTING US03**************")
#         date1 = "24 FEB 2019"
#         date2 = "13 MAY 2032"
#         date3 = "9 NOV 2011"
#         date4 = "6 OCT 1995"
#
#         self.assertEqual(US03(date1, date2), True)
#         self.assertEqual(US03(date2, date1), False)
#         self.assertEqual(US03(date3, date4), False)
#         self.assertEqual(US03(date4, date3), True)
#         self.assertEqual(US03(date4, date1), True)
#
#     def test_US04(self):
#         print("**************TESTING US04**************")
#         date1 = "24 FEB 2019"
#         date2 = "13 MAY 2032"
#         date3 = "9 NOV 2011"
#         date4 = "6 OCT 1995"
#
#         self.assertEqual(US04(date1, date2), True)
#         self.assertEqual(US04(date2, date1), False)
#         self.assertEqual(US04(date3, date4), False)
#         self.assertEqual(US04(date4, date3), True)
#         self.assertEqual(US04(date4, date1), True)


class test_US39(unittest.TestCase):

    def test_noUpcomingAnn(self):
        list_of_fams = [Family(familyid='01', marriagedate='15 JUN 1990'),
                        Family(familyid='02', marriagedate='16 MAY 2018'),
                        Family(familyid='03', marriagedate='1 JAN 2000')]
        self.assertListEqual(US39(list_of_fams), [])

    def test_upcomingAnn(self):
        list_of_fams = [Family(familyid='01', marriagedate='15 JUN 1990'),
                        Family(familyid='02', marriagedate='21 APR 2018'),
                        Family(familyid='03', marriagedate='1 JAN 2000')]
        self.assertListEqual(US39(list_of_fams), ['02'])

    def test_multipleUpcomingAnn(self):
        list_of_fams = [Family(familyid='01', marriagedate='21 APR 1990'),
                        Family(familyid='02', marriagedate='22 APR 2018'),
                        Family(familyid='03', marriagedate='23 APR 1995')]
        self.assertListEqual(US39(list_of_fams), ['01', '02', '03'])


class test_US42(unittest.TestCase):

    def test_US42(self):



if __name__ == '__main__':
    unittest.main()
