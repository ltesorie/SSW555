# Madeline Rys
# Unit Tests for User Stories

import unittest

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

# Test US10
from Functions import marriage_after_14
class TestsMarriageBefore14(unittest.TestCase):
	# def marriage_after_14(name, marrdate, birthdate):
	#     # Known Bug: Does not account for Leap years!
	#     result = True
	#     try:
	#         birth = datetime.strptime(birthdate, '%d %b %Y')
	#         if marr != 'NA':
	#             marr = datetime.strptime(marrdate, '%d %b %Y')
	#             marr_age = marr - birth
	#             result = marr_age > (timedelta(days=365) * 14)
	#         if result == False:
	#             print("Error - US10: ", name, " was married before age 14! ")
	#     except:
	#         result = False
	#     finally:
	#         return result
	def test_valid_dates(self):
		# valid date inputs
		# person is married before age 14
		self.assertTrue(marriage_after_14(name="Married After 14", marrdate='1 JAN 2015', birthdate='1 JAN 2000'))

	def test_invalid_dates(self):
		# invalid date inputs
		# person is married after age 14
		self.assertFalse(marriage_after_14(name="Married Before 14", marrdate='1 JAN 2013', birthdate='1 JAN 2000'))

	def test_14_exactly(self):
		# invalid date inputs
		# checks if return false when person is exactly 14
		self.assertFalse(marriage_after_14(name="Married at 14 Exactly", marrdate='1 JAN 2014', birthdate='1 JAN 2000'))

	def test_no_marrdate(self):
		# no marriage date
		# should return true since they were not married before 14
		self.assertTrue(marriage_after_14(name='Unmarried', marrdate='NA', birthdate='1 JAN 2000'))

# Test US12
from temp import parents_not_too_old
class TestParentsNotTooOld(unittest.TestCase):
	# def parents_not_too_old(child_age, mom_age, dad_age):
	# 	try:
	# 		result = true
	# 		mom_diff = mom_age - child_age
	# 		dad_diff = dad_age - child_age
	# 		if mom_diff > 60:
	# 			result = false
	# 			print("US 12 Error - Mom's age of ", mom_age, " is more than 60 years older than her child's age of ", child_age, " making it impossible!")

	# 		if dad_diff > 80:
	# 			result = false
	# 			print("US 12 Error - Dad's age of ", dad_age, " is more than 80 years older than his child's age of ", child_age, " making it impossible!")
		
	# 	except:
	# 		# Will return false due to error in format
	# 		result = false
		
	# 	finally:
	# 		return result

	def test_valid_ages(self):
		# valid dates
		# parents are reasonable ages older than their child
		self.assertTrue(parents_not_too_old(child_age = 20, mom_age = 50, dad_age = 50))

	def test_both_invalid_ages(self):
		# invalid ages
		# parents both too much older than child
		self.assertFalse(parents_not_too_old(child_age = 20, mom_age = 100, dad_age = 110))

	def test_mom_invalid(self):
		# invalid ages
		# mom too much older than child
		self.assertFalse(parents_not_too_old(child_age = 20, mom_age = 100, dad_age = 50))

	def test_dad_invalid(self):
		# invalid ages
		# dad too much older than child
		self.assertFalse(parents_not_too_old(child_age = 20, mom_age = 50, dad_age = 110))

	def test_cusp_ages(self):
		# valid ages
		# parents both on cusp of being too much older than child, should still return true
		self.assertTrue(parents_not_too_old(child_age = 20, mom_age = 80, dad_age = 100))

	def test_bad_format(self):
		# invalid ages
		# should return false since arguments are not subtractable
		self.assertFalse(parents_not_too_old(child_age = 'Hi', mom_age = "Bye", dad_age = 'Bad'))



# RUN TESTS

if __name__ == '__main__':
    unittest.main()
