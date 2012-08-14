#!/usr/bin/python

# Challenge: http://www.reddit.com/r/dailyprogrammer/comments/xxbbo/882012_challenge_86_easy_runlength_encoding/
# Solution: http://www.reddit.com/r/dailyprogrammer/comments/xxbbo/882012_challenge_86_easy_runlength_encoding/c5qf7af
# Run code online: http://ideone.com/DwxRr

import sys
import re

if len(sys.argv) == 1:
    print 'Enter a string as input'
    exit()

input = sys.argv[1]

items = []
idx = 0

while idx < len(input):
	char = input[idx]
	pattern = re.compile(r"[^" + char + "]")
	match = pattern.search(input, idx)
	if match:
		items.append( (match.start() - idx, char) )
		idx = match.start()
	else:
		items.append( (len(input) - idx, char) )
		break

print items

bonus = ''
for item in items:
	bonus += item[0] * item[1]

print bonus

# Sample Input:
# $ ./script.py 'Heeeeelllllooooo nurse!'
# [(1, 'H'), (5, 'e'), (5, 'l'), (5, 'o'), (1, ' '), (1, 'n'), (1, 'u'), (1, 'r'), (1, 's'), (1, 'e'), (1, '!')]

# Note that the above includes spaces and exclamation marks (which the original post does not?)
# Also I tried it using this reg-ex approach which is probably not as efficient as just going through each character in the string, but I wanted to try it this way :D

# Other sample:
# $ ./script.py '!!!!!!!!!!!lol!!!!!!!!!!!!!!!'
# [(987, '!'), (1, 'l'), (1, 'o'), (1, 'l'), (1201, '!')]
# ( I didn't include all the 2000+ exclamation marks above :)

# BONUS, output the result back to normal format again:
# bonus = ''
# for item in items:
#     bonus += item[0] * item[1]

# print bonus # 'Heeeeelllllooooo nurse!'