# Author: Alyson Randall
# User Story Tests

import unittest
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from Functions import US03, US04, US06, US18, US29, US36
import Project03 as p3

class test(unittest.TestCase):
    def test_US03(self):
        print("**************TESTING US03**************")
        date1 = "24 FEB 2019"
        date2 = "13 MAY 2032"
        date3 = "9 NOV 2011"
        date4 = "6 OCT 1995"

        self.assertEqual(US03(date1, date2), True)
        self.assertEqual(US03(date2, date1), False)
        self.assertEqual(US03(date3, date4), False)
        self.assertEqual(US03(date4, date3), True)
        self.assertEqual(US03(date4, date1), True)

    def test_US04(self):
        print("**************TESTING US04**************")
        date1 = "24 FEB 2019"
        date2 = "13 MAY 2032"
        date3 = "9 NOV 2011"
        date4 = "6 OCT 1995"

        self.assertEqual(US04(date1, date2), True)
        self.assertEqual(US04(date2, date1), False)
        self.assertEqual(US04(date3, date4), False)
        self.assertEqual(US04(date4, date3), True)
        self.assertEqual(US04(date4, date1), True)

    def test_US06(self):
        print("**************TESTING US06**************")
        husbDeath1 = "24 FEB 2019"
        husbDeath2 = "13 MAY 2032"
        husbDeath3 = "9 NOV 2011"
        wifeDeath1 = "01 NOV 1995"
        wifeDeath2 = "17 DEC 1996"
        wifeDeath3 = "26 MAR 2013"
        wifeDeath4 = "26 MAR 2019"
        divorceDate1 = "01 JAN 2018"
        divorceDate2 = "02 FEB 2035"
        divorceDate3 = "01 NOV 1990"

        self.assertEqual(US06(husbDeath1, wifeDeath1, divorceDate1), True)
        self.assertEqual(US06(husbDeath2, wifeDeath2, divorceDate2), True)
        self.assertEqual(US06(husbDeath3, wifeDeath3, divorceDate3), False)
        self.assertEqual(US06(husbDeath3, wifeDeath4, divorceDate1), True)

    def test_US18(self):
        print("**************TESTING US18**************")

    def test_US36(self):
        print("**************TESTING US36**************")

        date1 = "01 JAN 2019"
        date2 = "02 FEB 1999"
        date3 = "03 MAR 2011"

        self.assertEqual(US36(date1), True)
        self.assertEqual(US36(date2), False)
        self.assertEqual(US36(date3), False)


class testRecentDeath(unittest.TestCase):
    print("**************TESTING US29**************")

    def testNotRecentlyDeceased(self):
        today = datetime.today()
        fourHundredDays = timedelta(days=400)
        fourHundredDaysAgo = today - fourHundredDays
        str400DaysAgo = fourHundredDaysAgo.strftime('%d %b %Y')
        individual = {'DEAT': str400DaysAgo}
        self.assertFalse(US29(individual))

    def testRecentlyDeceased(self):
        today = datetime.today()
        twoDays = timedelta(days=2)
        twoDaysAgo = today - twoDays
        str2DaysAgo = twoDaysAgo.strftime('%d %b %Y')
        individual = {'DEAT': str2DaysAgo}
        self.assertTrue(US29(individual))

    def testLiving(self):
        today = datetime.today()
        individual = {'DEAT': "NA"}
        self.assertFalse(US29(individual))



if __name__ == '__main__':
    unittest.main()
