#Laura Tesoriero
#Unittests

import unittest
import datetime

class testAge(unittest.TestCase):

    def test_utc(self):
        if self.validtags == 'DATE' is True:
            self.assertequal(self.argument,datetime.utcnow())


if __name__ == 'Project3_AR':
    unittest.main()

