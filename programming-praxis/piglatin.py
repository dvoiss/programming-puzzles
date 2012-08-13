#!/usr/bin/env python

# convert english to pig-latin and pig-latin to english
# solution for: http://programmingpraxis.com/2009/06/02/pig-latin/2/

# rules:
# words that start with a consonant and followed immediately by a vowel,
# such as 'sorry' become 'orry-say', (first letter plus 'ay')
# words that start with vowels: 'amazing' => 'amazing-way' ('way' is appended)

# special case:
# in a word such as 'wonderful', it becomes 'onderful-way',
# son conversion back into english, 'onderful-way' would get recognized
# as a word that starts with a vowel because it has the 'way' at the end:
# 'onderful-way' => 'onderful'

def pigify(text):
	'''Convert English to Pig Latin

		>>> text = "Hello there good sir! What a great day!"
		>>> pigify( text )
		'ello-Hay ere-thay ood-gay ir!-say at-Whay a-way eat-gray ay!-day'
	'''

	vowels = list("aeiouAEIOU")

	def pigify_word(word):
		if word[0] in vowels:
			return word + "-way"
		else:
			collection = [word.find(item) for item in vowels if word.find(item) != -1]
			idx = 1 if len(collection) == 0 else min(collection)
			return word[idx:] + "-" + word[:idx] + "ay"

	return " ".join([pigify_word(word) for word in text.split(" ")])

def englify(text):
	'''Convert Pig Latin to English

		>>> text = "ello-Hay ere-thay ood-gay ir!-say at-Whay a-way eat-gray ay!-day"
		>>> englify( text )
		'Hello there good sir! What a great day!'
	'''
	def englify_word(word):
		if word[-4:] == "-way":
			return word[:-4]
		else:
			return word.split("-")[1][:-2] + word.split("-")[0]

	return " ".join([englify_word(word) for word in text.split(" ")])

if __name__ == '__main__':
	import doctest
	print doctest.testmod()

	print ''
	test = "Hello there good sir! What a great day!"
	pigified = pigify(test)
	print "ORIGINAL:     " + test
	print "TO PIG LATIN: " + pigified
	print "TO ENGLISH:   " + englify(pigified)