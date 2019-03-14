# Madeline Rys
# Unit Tests for User Stories

import unittest
from Project03 import *

#Test US08
from Functions import  birth_before_marriage
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
from Functions import birth_before_death
class TestBirthBeforeDeath(unittest.TestCase):
	# User Story 09 - Madeline Rys: checks birth date of child to ensure it is before death of either parent
	# def birth_before_death(birthdate, momdeath, daddeath):
	#     result = True

	#     try:
	#         birth = datetime.strptime(birthdate, '%d %b %Y')

	#         if momdeath == 'NA' and daddeath == 'NA':
	#             result = True
	#         elif momdeath == 'NA':
	#             dad = datetime.strptime(daddeath, '%d %b %Y')
	#             dad9months = dad - relativedelta(months=9)
	#             if dad9months < birth:
	#                 print("Error - US09: child's birth date ", str(birthdate) + " is after father's death date ", str(daddeath))
	#                 result = False
	#         elif daddeath == 'NA':
	#             mom = datetime.strptime(momdeath, '%d %b %Y')
	#             if mom < birth:
	#                 result = False
	#                 print("Error - US09: child's birth date ", str(birthdate) + " is after mother's death date ", str(momdeath))
	#         else:
	#             dad = datetime.strptime(daddeath, '%d %b %Y')
	#             dad9months = dad - relativedelta(months=9)
	#             mom = datetime.strptime(momdeath, '%d %b %Y')
	#             if birth > mom and birth > dad9months:
	#                 result = False
	#                 print("Error - US09: child's birth date ", str(birthdate) + " is after parents' death dates ",
	#                       str(momdeath), str(daddeath))
	    
	#     except:
	#         print("Error - US09: one of the dates given was in the incorrect format")
	#         result = False
	    
	#     finally:
	#         return result

	def test_valid_dates(self):
		# valid date inputs
		# mom and dad die more than one year after child's birth, making both dates valid
		self.assertTrue(birth_before_death(birthdate='31 DEC 1999', momdeath='1 JAN 2000', daddeath='1 JAN 2000'))

	def test_no_deaths(self):
		# valid date inputs
		# mother and father both still alive, meaning they did not die before child's birth
		self.assertTrue(birth_before_death(birthdate='31 DEC 1999', momdeath='NA', daddeath='NA'))

	def test_invalid_mom_date(self):
		# invalid date inputs
		# mom dies day before child's birth
		self.assertFalse(birth_before_death(birthdate='31 DEC 1999', momdeath='30 DEC 1999', daddeath='NA'))

	def test_invalid_dad_date(self):
		# invalid date inputs 
		# dad dies a year before child's birth
		self.assertFalse(birth_before_death(birthdate='31 DEC 1999', momdeath='NA', daddeath='31 DEC 1998'))

	def test_both_invalid(self):
		# invalid date inputes
		# mom and dad both dead before birth
		self.assertFalse(birth_before_death(birthdate='31 DEC 1999', momdeath='31 DEC 1998', daddeath='31 DEC 1998'))

if __name__ == '__main__':
    unittest.main()
