#!/usr/bin/python

# For the reddit daily programmer challenge

# Challenge: http://www.reddit.com/r/dailyprogrammer/comments/y5svk/8132012_challenge_88_intermediate_printing_out_a/
# Solution: http://www.reddit.com/r/dailyprogrammer/comments/y5svk/8132012_challenge_88_intermediate_printing_out_a/c5soy7s
# run code at http://ideone.com/yFOA4
# by @dvoiss on github / @daveasaurus on reddit

# Two variations:
# the first simply uses the calendar module's print capability:
# the second uses calendar module for localized month name and day abbreviations 
#   and for getting the days in a month, the output is printed using format strings

import calendar
import sys

year, month = int(sys.argv[1]), int(sys.argv[2])

# 1. use built in method:
print '\n'.join( calendar.month(year, month).split('\n') )

# 2. see reddit comment for more info
separator_string = '+' + '-'*20 + '+'
def print_cal(month, year):
	month_days = [ '' if i == 0 else str(i) for i in calendar.Calendar(0).itermonthdays(year, month) ]

	print separator_string + '\n|' + str.center( calendar.month_name[month], 20 ) + '|\n' + separator_string
	print '|' + "".join(['{' + str(i) + ':<2}|' for i in range(0, 7) ]).format(*map(lambda x: x[0] + ' ', calendar.day_abbr))
	print separator_string
	print "".join([('|{' if j % 7 == 0 else '{') + str(i + j + (6 * i)) + ':<2}|'
		+ ('\n' if j % 7 == 6 and i != (len(month_days) / 7 - 1) else '') for i in range(0, len(month_days) / 7) for j in range(0, 7)]).format(*month_days)
	print separator_string

print_cal(month, year)