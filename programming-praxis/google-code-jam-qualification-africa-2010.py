# programming praxis:
# http://programmingpraxis.com/2011/02/15/google-code-jam-qualification-round-africa-2010/
# Today's three programming exercises come from the Google Code Jam Qualification Round Africa 2010

# 1.
# find the index of the two items that add up to the total credit amount
def store_credit(sample, credit):
	for i, x in enumerate(sample):
		for j, y in enumerate(sample):
			if x + y == credit and i != j:
				return (i, j)

# test cases:
print "1. Store credit"
print store_credit( [2, 1, 9, 4, 4, 56, 90, 3], 8 )			# (3, 4) (indexed at 0)
print store_credit( [150, 24, 79, 50, 88, 345, 3], 200 )	# (0, 3)
print store_credit( [5, 75, 25], 100 )						# (1, 2)

# 2.
# reverse a string of words
# "This is a test" => "test a is This"

# using list data structure to split then reverse
def reverse_words_pythonic(input):
	return " ".join(input.split(" ")[::-1])

# using no reverse, split, or join,
# going character by character, using only strings and no data-structures:
def reverse_words(input, input_length):
	result = ""
	word = ""
	i = 0
	while i < input_length:
		char = input[i]
		if (char == ' '):
			result = ' ' + word + result
			word = ""
		else:
			word += char
		i += 1
	# add the final word:
	result = word + result
	return result

test = "This is a test"
print ""
print "2. Word Reversal (two variants)"
print reverse_words_pythonic(test)		# "test a is This"
print reverse_words(test, len(test))	# "test a is This"

# 3.
# T9 spelling, simulating entering text via a telephone
letters = 'abc def ghi jkl mno pqrs tuv wxyz'.split(' ')
numbers = range(2, 10)

# pass in a tuple: (2, 'abc') or (7, 'pqrs')
def convert_by_letter(item):
	dictionary = []
	for idx, val in enumerate(item[1]):
		dictionary.append( (val, str(item[0]) * (idx + 1)) )

	return dictionary

# match number to letters:
# zip: [(2, 'abc'), (3, 'def'), ... (7, 'pqrs'), (8, 'tuv'), (9, 'wxyz')]
# map letter to multiple numbers:
# map: [[('a', '2'), ('b', '22'), ('c', '222')] ... [('w', '9'), ('x', '99'), ('y', '999'), ('z', '9999')]]
# reduce to a single list of tuples instead of a list of lists
# reduce: [('a', '2'), ('b', '22'), ... ('y', '999'), ('z', '9999')]
# turn into a dictionary:
# dict: {'a': '2', 'c': '222', 'b': '22', ... 'x': '99', 'z': '9999'}
assembled_dict = dict(reduce(lambda x, y: x + y, map( convert_by_letter, zip(numbers, letters) )))

# all the lines above assemble the dictionary,
# the assembled_dict could just be hard-coded instead of being generated,
# but I wanted to generate it as a separate exercise

def encode_text(input):
	result = ""
	for i in input:
		if (i == ' '):
			# no spaces are required between sequential presses of '0'
			result += '0'
		else:
			char = assembled_dict[i]
			# spaces are required between sequential presses of a number
			# where a different letter is being typed (see "hi" below)
			if len(result) > 0 and char[-1] == result[-1]:
				result += ' '
			result += char
	return result

print ""
print "3. Text Encoding"
print encode_text("hi") 			# encoded as "44 444"
print encode_text("yes")			# encoded as "999337777"
print encode_text("foo  bar") 		# encoded as "333666 6660022 2777"
print encode_text("hello world") 	# encoded as "4433555 555666096667775553"