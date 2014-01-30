# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct ouptuts yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
        #I would never actually use parameters like this
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1 and year2/month2/day2. Assumes inputs are valid dates 
    in Gregorian calendar, and the first date is not after the second."""
    
    year_difference = year2 - year1
    month_difference = month2 - month1
    day_difference = day2 - day1
    
    #Number of year * number of days in a year
    yearsInDays = year_difference * 360
    monthsInDays = month_difference * 30
    
    #Checking for cases that are a year or less
    if (year_difference < 2):
        totalDays = abs(yearsInDays + (monthsInDays - day_difference))
        
    #Checking for cases greater than a year
    if (year_difference > 1):
        totalDays = yearsInDays + (monthsInDays - day_difference)
    
    return totalDays

#This procedure is the only reason I want to include this file, So I can refer to it later

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        print result
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()