# Coursera:
# Algorithms: Design and Analysis - Part 1

# merge-sort:
# modifies original lists

# Example:
# unsorted_list = [ 11, 3, 2, 1, 8, 7, 4, 3, 8, 34, 21 ]
# result = [1, 2, 3, 3, 4, 7, 8, 8, 11, 21, 34]
def sort( unsorted_list ):
	unsorted_len = len(unsorted_list)
	a = unsorted_list[ 0 : unsorted_len / 2 ]
	if ( len(a) != 1 ):
		a = sort( a )

	b = unsorted_list[ unsorted_len / 2 : ]
	if ( len(b) != 1 ):
		b = sort( b )

	return merge( a, b )

# Example:
# a = [ 2, 4, 5, 6, 7 ]
# b = [ 1, 2, 3, 4, 9, 11 ]
# result = [1, 2, 2, 3, 4, 4, 5, 6, 7, 9, 11]
def merge( a, b ):
	i, j = 0, 0
	a_len, b_len = len(a), len(b)
	result = []

	for k in range(a_len + b_len):
		if a_len != i and b_len != j:
			if a[i] < b[j]:
				result.append( a[i] )
				i += 1
			else:
				result.append( b[j] )
				j += 1
		elif a_len == i:
			result.append( b[j] )
			j += 1
		elif b_len == j:
			result.append( a[i] )
			i += 1

	return result

# test merge function:
a = [ 2, 4, 5, 6, 7 ]
b = [ 1, 2, 3, 4, 9, 11 ]
print "TESTING MERGE WITH: %s and %s" % (a, b)
result = merge(a, b)
print "RESULT OF MERGE TEST: %s" % result

print ""

# test sort function:
unsorted_list = [ 11, 3, 2, 1, 8, 7, 4, 3, 8, 34, 21 ]
print "TESTING SORT WITH: %s" % unsorted_list
result = sort( unsorted_list )
print "RESULT OF SORT: %s" % result