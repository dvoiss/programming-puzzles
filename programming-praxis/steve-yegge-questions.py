# http://programmingpraxis.com/2009/06/30/steve-yegges-phone-screen-coding-exercises/
# Steve Yegge's Phone screen questions

# reverse-string
# built-in in python: input[::-1] => "gnirts-tset"
def reverse_string(input, input_length):
	result = ""
	i = input_length - 1
	while i >= 0:
		result += input[i]
		i -= 1

	return result

test = "test-string"
print ""
print "1. Reverse a string"
print reverse_string(test, len(test)) # => 'gnirts-tset'


# compute Nth fibonacci number
def fibonacci(n):
	a, b = 0, 1
	i = 2
	while i < n:
		a, b = b, a + b
		i += 1

	return b

print ""
print "2. Calculate n-th fibonacci #"
print fibonacci(5)  # => 3
print fibonacci(8)  # => 13
print fibonacci(9)  # => 21


# multiplication tables
def print_table(n):
	format_string = " ".join(['{' + str(i) + ':<3}' for i in range(0, n)])
	for i in range(1, n + 1):
		print format_string.format(*[ i * j for j in range(1, n + 1) ])

# one-liner (using format_string above):
# print "\n".join([ format_string.format(*[ i * j for j in range(1, 13) ]) for i in range(1, 13) ])

test = 12
print ""
print "3. Print multiplication table %s x %s" % (test, test)
print_table(test)


# assumes the file has one integer per line and no blank lines / errors
def sum_integers_line_by_line(file_path):
	return sum( map( lambda x: int(x), open(file_path).readlines() ) )

print ""
print "4. Sum up integers in a file"
print sum_integers_line_by_line('input/integers.txt')


def odds(start, end):
	return " ".join([ str(i) for i in range(start, end + 1) if i % 2 == 1 ])

print ""
print "5. Print the odd numbers from 1 to 99"
print odds(1, 99)


# find the largest int in an array (not using max function)
def find_largest(list):
	# return max( list ) # using built-in max function
	largest = list[0]
	for i in range(1, len(list)):
		if list[i] > largest:
			largest = list[i]

	return largest

test = [2, 33, 20, 1, 234, 23, 21, 54, 233, 120]
print ""
print "6. Find the largest int in an array"
print "Test values: %s" % test
print find_largest(test)


# format an RGB value as a 6-digit hexadecimal string
def hex_string(values):
	# using built-in format strings:
	# return "#" + "".join([ "{0:x}".format(item) for item in values ])
	hex_values = list('0123456789abcdef')
	return "#" + "".join( map( lambda x: hex_values[x/16] + hex_values[x%16], values ) )

test = [255, 128, 31] # ff801f
print ""
print "7. Convert RGB values to a hex-string"
print "Test values: %s" % test
print hex_string(test)