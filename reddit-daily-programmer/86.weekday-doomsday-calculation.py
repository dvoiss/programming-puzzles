#!/usr/bin/python

# Challenge: http://www.reddit.com/r/dailyprogrammer/comments/xx97s/882012_challenge_86_intermediate_weekday/
# Solution: http://www.reddit.com/r/dailyprogrammer/comments/xx97s/882012_challenge_86_intermediate_weekday/c5qgu1k
# Run code online: http://ideone.com/HIyf7

# Sample Input
# $ python challenge86intermediate.py '4/1/1111'
# Saturday

# $ python challenge86intermediate.py '2/15/2000'
# Tuesday

# $ python challenge86intermediate.py '5/24/-200'
# Thursday

# For pre-gregorian calendar dates so there is a separate 
# calculation performed (is_gregorian is false).

# Confusion exists due to a lack of sample inputs (see Reddit thread)

import sys

# this example assumes proper dates are entered (there are no safety checks performed)
if len(sys.argv) == 1:
    print 'Enter a date string as input in the format month/day/year'
    print 'Example: January 17, 1981 is inputted as "1/17/1981"'
    exit()

# split string and convert to integers
month, day, year = map( lambda x: int(x), sys.argv[1].split('/') )

# gregorian?
is_gregorian = True
if (year < 0):
	is_gregorian = False
	year = year - 1 # account for there being no year zero
else:
	from datetime import date
	julian_calendar_fail = date(1582, 10, 15) # julian calendar goes away
	is_gregorian = date(year, month, day) > julian_calendar_fail

# leap year calculation:
if is_gregorian and year % 4 == 0 and not ( year % 100 == 0 and year % 400 != 0 ):
	is_leap_year = True
elif not is_gregorian and year % 4 == 0: # julian
	is_leap_year = True
else:
	is_leap_year = False

if (month == 2):
	days_in_month = 29 if is_leap_year else 28
else:
	from calendar import monthrange
	days_in_month = monthrange(2000, month) # year irrelevant for non-February months

# safety:
century = int( str(year)[:-2] ) if str(year)[:-2] != '' else 0
year    = int( str(year)[-2:] ) if str(year)[-2:] != '' else 0

# the doomsday calculation: http://en.wikipedia.org/wiki/Doomsday_rule
doomsdays = [ 4 if is_leap_year else 3, 29 if is_leap_year else 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12 ]
# weekdays, starting with Monday == 0
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

d = ( (year / 12) + (year % 12) + (b / 4) )

# "Finding a year's Doomsday" section @ http://en.wikipedia.org/wiki/Doomsday_rule:
if is_gregorian:
	d = d % 7

	anchor_days = [ 1, 6, 4, 2 ] # from wikipedia link above
	anchor = anchor_days[ century % 4 ]
	offset = day - doomsdays[ month - 1 ]
	day_of_week = (d + anchor + offset)
else:
	anchor = 6 + d - century
	anchor += 7 if anchor < 0 else -7 # normalize between -7 and 7
	offset = day - doomsdays[ month - 1 ]
	day_of_week = (anchor + offset)

# normalize day_of_week to be between 0 and 6
day_of_week = day_of_week % 7
print days[ day_of_week ]