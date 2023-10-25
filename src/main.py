def new_method_which_is_not_relevant():
    #Just a method to check if tests run when commited
    number = 1 + 1

def just_another_dummy_method():
    # Just a method to check if tests run when commited
    number = 1 + 1

def check_divisible_by_4_but_not_100(year):
   is_leap = False

   if (year % 4 == 0) and (year % 100 != 0):
      is_leap = True

   return is_leap

def check_divisible_by_400(year):
   is_leap = False

   if year % 400 == 0:
      is_leap = True

   return is_leap

def check_not_divisible_by_4(year):
   is_leap = False

   if year % 4 != 0:
      is_leap = True

   return is_leap

def check_divisible_by_100_but_not_400(year):
    is_leap = False

    if (year % 100 == 0) and (year % 400 != 0):
        is_leap = True

    return is_leap

def isLeapYear(year):
    is_leap_year = False

    if check_divisible_by_4_but_not_100(year) == True:
        is_leap_year = True

    if check_divisible_by_400(year) == True:
        is_leap_year = True

    return is_leap_year



# Looping through an array of years to verify the function works properly
years = [1700,2000,2024,1973,1992,1862]

for year in years:
    if isLeapYear(year) == True:
        leap_string = "is a leap year."
    else:
        leap_string = "is not a leap year"

    print(f"The year {year} {leap_string}")


