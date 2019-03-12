# Madeline Rys
# Unit Tests for User Stories

import unittest
from Project03 import *

#Test US08
class TestBirthBeforeMarriage(unittest.TestCase):
	# User Story 08 - Madeline Rys: checks birth date of child to ensure it is after marriage of parents
	# def birth_before_marriage(birthdate, marrdate):
	#     birth = datetime.strptime(birthdate, '%d %b %Y')
	#     if marrdate != 'NA':
	#         marr = datetime.strptime(marrdate, '%d %b %Y')

	#         if birth < marr:
	#             print("Error - US08: child's birth date ", str(birthdate) + " is before parents' marriage date ",
	#                   str(marrdate))
	#         return birth < marr
	def test_valid_dates(self):
		# valid date inputs
		# child's birth is after marents' marriage
		self.assertTrue(birth_before_marriage(birthdate='1 JAN 2000', marrdate='31 DEC 1999'))

	def test_invalid_dates(self):
		# invalid date inputs
		# child's birth is before parent's marriage
		self.assertFalse(birth_before_marriage(birthdate='31 DEC 1999', marrdate='1 JAN 2000'))

	def test_same_date(self):
		# invalid date inputs
		# child's birth is same date as parents' marriage
		self.assertFalse(birth_before_marriage(birthdate='1 JAN 2000', marrdate='1 JAN 2000'))

	def test_no_marriage_date(self):
		#invalid date inputs
		#child's parentsh ave no marriage date, therefore cannot be born after marriage
		self.assertFalse(birth_before_marriage(birthdate='1 JAN 2000', marrdate='NA'))

	def test_invalid_date_format(self):
		# invalid date format
		# args are dates that aren't dates
		self.assertRaises(ValueError, birth_before_marriage, 'NA', 'NA')

#Test US09

if __name__ == '__main__':
    unittest.main()
