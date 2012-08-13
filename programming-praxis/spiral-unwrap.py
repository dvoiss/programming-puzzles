# http://programmingpraxis.com/2010/06/01/unwrapping-a-spiral/
# Unwrapping A Spiral

#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16
# 17 18 19 20

# input assumption:
# spiral is given in a 2-dimensional array:
# [[1,   2,  3,  4],  
#  ...
#  [17, 18, 19, 20]]
#
# should yield:
# [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10]

# this solution is intended to take up as little space as possible,
# and as such it pops items off the array, destroying the original:
def unwrap(input):
	result = []
	while True:
		try:
			# to the right:
			result += input.pop(0)

			# down:
			for i in range(0, len(input)):
				result.append( input[i].pop() )

			# left:
			result += input.pop()[::-1]

			# up:
			for i in range(0, len(input))[::-1]:
				result.append( input[i].pop(0) )

		except IndexError:
			break

	return result

# build the matrix according to format above:
def build_test(columns, rows):
	return [ range(i * columns + 1, i * columns + columns + 1) for i in range(0, rows) ]

# tests:
print unwrap( build_test(4, 5 ) )
print unwrap( build_test(2, 16) )
print unwrap( build_test(3, 8 ) )