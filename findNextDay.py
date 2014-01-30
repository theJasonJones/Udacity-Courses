### Define a simple nextDay procedure, that assumes every month has 30 days.

#Procedure that moves a day up one day
#Checks for the end of the month and the end of the year
def nextDay(year, month, day):
  day += 1

  if (day > 30):
    day = 1
    month += 1

  if (month > 12):
    month = 1
    year += 1

  return year, month, day

#Test cases to make sure the procedure was implemented correctly
print nextDay(1999, 12, 30)
### Expected output (2000, 1, 1)

print nextDay(2013, 1, 30)
### Expected output (2013, 2, 1)

print nextDay(2012, 12, 30)
### Expected output (2013, 1, 1)