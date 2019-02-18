#Laura Tesoriero
#Unittests

import unittest
import datetime


class TestDates(unittest.TestCase):

    def test_utc(self):
        if self.validtags == 'DATE' is True:
            self.assertequal(self.argument,datetime.utcnow())


class TestAge(unittest.TestCase):

    def test_Age(self):
        if self.validtags == 'DATE' is True:
            self.assertequal(self.argument,datetime.utcnow())


if __name__ == '__main__':
    unittest.main()

