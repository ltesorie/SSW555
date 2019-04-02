from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


# User Story 1 - Laura T: checks dates to make sure it has occurred
def date_before_now(date):
    tbv_date = datetime.strptime(date, '%d %b %Y')
    today = datetime.now()
    if not tbv_date <= today:
        print("Error:" + str(date) + "is after current date" + str(today))
    return tbv_date < today


# User Story 03 - Alyson Randall: checks that birth date occurs before death date
def US03(birth_date, death_date):
    if birth_date and death_date != 'NA':
        birth = datetime.strptime(birth_date, '%d %b %Y')
        death = datetime.strptime(death_date, '%d %b %Y')
        if death < birth:
            print("Error - US03: Individuals's birth date ", str(birth_date), " occurs after death date ", str(death_date))
        return death > birth


# User Story 04 - Alyson Randall: checks that a couple is married before getting a divorce
def US04(marr_date, div_date):
    if marr_date and div_date != 'NA':
        marriage = datetime.strptime(marr_date, '%d %b %Y')
        divorce = datetime.strptime(div_date, '%d %b %Y')
        if divorce < marriage:
            print("Error - US04: Marriage date ", str(marr_date), " occurs after divorce date ", str(div_date))
        return divorce > marriage


# User Story 06 - Alyson Randall: checks that divorce date occurs before death date
def US06(husband, wife, divorce_date):
    if divorce_date != 'NA':
        divorce = datetime.strptime(divorce_date, '%d %b %Y')
        husband_death = datetime.strptime(husband, '%d %b %Y')
        wife_death = datetime.strptime(wife, '%d %b %Y')
        if husband_death < divorce and wife_death < divorce:
            print("Error - US06: Divorce date", str(divorce_date), " occurs after husband and wife's death dates", str(husband), "and", str(wife), "respectively")
            return True
        if husband_death < divorce:
            print("Error - US06: Divorce date", str(divorce_date), " occurs after husband's death date ", str(husband))
            return True
        if wife_death < divorce:
            print("Error - US06: Divorce date", str(divorce_date), " occurs after wife's death date ", str(wife))
            return True
        return False



# User Story 08 - Madeline Rys: checks birth date of child to ensure it is after marriage of parents
def birth_before_marriage(birthdate, marrdate):
    birth = datetime.strptime(birthdate, '%d %b %Y')
    if marrdate != 'NA':
        marr = datetime.strptime(marrdate, '%d %b %Y')

        if birth < marr:
            print("Error - US08: child's birth date ", str(birthdate) + " is before parents' marriage date ",
                  str(marrdate))
        return birth > marr
    else:
        return False


# User Story 09 - Madeline Rys: checks birth date of child to ensure it is before death of either parent
def birth_before_death(birthdate, momdeath, daddeath):
    result = True

    try:
        birth = datetime.strptime(birthdate, '%d %b %Y')

        if momdeath == 'NA' and daddeath == 'NA':
            result = True
        elif momdeath == 'NA':
            dad = datetime.strptime(daddeath, '%d %b %Y')
            dad9months = dad - relativedelta(months=9)
            if dad9months < birth:
                print("Error - US09: child's birth date ", str(birthdate) + " is after father's death date ", str(daddeath))
                result = False
        elif daddeath == 'NA':
            mom = datetime.strptime(momdeath, '%d %b %Y')
            if mom < birth:
                result = False
                print("Error - US09: child's birth date ", str(birthdate) + " is after mother's death date ", str(momdeath))
        else:
            dad = datetime.strptime(daddeath, '%d %b %Y')
            dad9months = dad - relativedelta(months=9)
            mom = datetime.strptime(momdeath, '%d %b %Y')
            if birth > mom and birth > dad9months:
                result = False
                print("Error - US09: child's birth date ", str(birthdate) + " is after parents' death dates ",
                      str(momdeath), str(daddeath))
    
    except:
        print("Error - US09: one of the dates given was in the incorrect format")
        result = False
    
    finally:
        return result


# User Story 18 - Alyson Randall: Siblings should not marry
def US18(sibDad, sibMom, list_of_fams):
    for fam in list_of_fams:
        if sibDad in fam.CHIL:
            husband_fam = fam
        if sibMom in fam.CHIL:
            wife_fam = fam
            if husband_fam == wife_fam:
                print("Error - US18: Siblings", sibDad, "and", sibMom, "should not be married.")
                return True
            return False

# User Story 10 - Madeline Rys: People should not marry before age 14
def marriage_after_14(name, marrdate, birthdate):
    # Known Bug: Does not account for Leap years!
    result = True
    try:
        birth = datetime.strptime(birthdate, '%d %b %Y')
        if marrdate != 'NA':
            marr = datetime.strptime(marrdate, '%d %b %Y')
            marr_age = marr - birth
            result = marr_age > (timedelta(days=5114))
            if result == False:
                print("Error - US10: ", name, " was married before age 14! ")
    except:
        result = False
    finally:
        return result


# US 21 - correct gender role
def correct_gender_role(gender, husb, wife):
    for indi in gender:
        if indi == "F":
            if wife != "WIFE":
                print("Error - US21: Incorrect gender for :" + wife + "please correct")
                return False
            elif wife == "NA":
                pass
        if indi == "M":
            if husb != "HUSB":
                print("Error - US21: Incorrect gender for :" + husb + "please correct")
                return False
            elif husb == "NA":
                pass


#US 15 Children Check
def children_limit(family_list):
    for kids in family_list:
        if len(kids.CHIL) >= 15:
            print("Error - US15: Family ", kids, " has 15 or more children.")

# User Story 12 - Madeline Rys: Parents not too old
# Mother should be less than 60 years older than her children and father should be less than 80 years older than his children
# Returns true if parents are not too old, false if they are
def parents_not_too_old(child_age, mom_age, dad_age):
    result = True
    try:
        mom_diff = mom_age - child_age
        dad_diff = dad_age - child_age
        if mom_diff > 60:
            result = False
            print("Error - US12: Mom's age of ", mom_age, " is more than 60 years older than her child's age of ", child_age, " making it impossible!")

        if dad_diff > 80:
            result = False
            print("Error - US12: Dad's age of ", dad_age, " is more than 80 years older than his child's age of ", child_age, " making it impossible!")
    
    except:
        # Will return false due to error in format
        result = False
    
    finally:
        return result

# User Story 28 - Madeline Rys: Order siblings by age
# List siblings in families by decreasing age, i.e. oldest siblings first
# Returns Siblings in a list ordered by age
def order_siblings_by_age(list_of_children, list_of_indis):
    siblings_in_order = []
    try:
        # code goes here
        children_and_ages = []
        for chil in list_of_children:
            for indi in list_of_indis:
                if indi.INDI == chil:
                    children_and_ages.append((chil, indi.AGE))
        #sort children_and_ages by age
        for child in children_and_ages:
            siblings_in_order.append(child[0])
    except:
        print("Error when sorting siblings")
    finally:
        return siblings_in_order

# User Story 31 - Madeline Rys: List Living Single
# List all living people over 30 who have never been married in a GEDCOM file
# Returns a list of the INDI ids of all those living single
def list_living_single(list_of_indis):
    living_single = []
    try:
        # code goes here
        for indi in list_of_indis:
            if indi.AGE > 30:
                if indi.FAMS == 'NA':
                    living_single.append(indi.INDI)
    except:
        print("Error while trying to list living single")
    finally:
        return living_single
