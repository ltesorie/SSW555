# Laura Tesoriero
# Unittests
# test US01

import unittest
import datetime
from Project03 import *


class TestDateStructure(unittest.TestCase):

    def test_date_structure(self):
        self.assertTrue(date_before_now(self))


#class TestExistence(unittest.TestCase):

#    def test_existence(self):
#        if self.validtags == 'DATE' is True:
#            self.assertequal(self.argument, datetime.utcnow())


# class TestBadDate(unittest.TestCase):

#    def test_bdate(self):
#        if self.validtags == 'DATE' is True:
#            self.assertequal(self.argument, datetime.utcnow())


# class TestGoodDate(unittest.TestCase):

#    def test_gdate(self):
#        if self.validtags == 'DATE' is True:
#            self.assertequal(self.argument, datetime.utcnow())


# class TestDateToday(unittest.TestCase):

#    def test_Today(self):
#        if self.validtags == 'DATE' is True:
#            self.assertequal(self.argument, datetime.utcnow())


if __name__ == '__main__':
    unittest.main()

