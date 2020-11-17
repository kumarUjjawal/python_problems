# Return true if the given input is a leap year else return false.

def leap_year(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 == 0 and year % 400 == 0):
                leap =  True
        else:
            leap = False
    else:
        leap = False
    return leap
   

years = int(input())
print(leap_year(years))




