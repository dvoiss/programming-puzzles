from string import ascii_uppercase as up

def encode(text, cipher, decode=False):
	result, cipher_index, decode = '', 0, -1 if decode else 1
	for i, x in enumerate(text):
		result += up[(up.index(x) + (decode * up.index(cipher[cipher_index % len(cipher) ]))) % 26]
		cipher_index += 1
	return result

	return ''.join([up[(up.index(x) + (decode * up.index(cipher[ ci % len(cipher) ]))) % 26] for ci in range(max(len(cipher), len(text))) for i, x in enumerate(text)])

print encode("THECAKEISALIE", "GLADOS", False)
print encode("ZSEFOCKTSDZAK", "GLADOS", True)

HSULAREFOTXNMYNJOUZWYILGPRYZQVBBZABLBWHMFGWFVPMYWAVVTYISCIZRLVGOPGBRAKLUGJUZGLNBASTUQAGAVDZIGZFFWVLZSAZRGPVXUCUZBYLRXZSAZRYIHMIMTOJBZFZDEYMFPMAGSMUGBHUVYTSABBAISKXVUCAQABLDETIFGICRVWEWHSWECBVJMQGPRIBYYMBSAPOFRIMOLBUXFIIMAGCEOFWOXHAKUZISYMAHUOKSWOVGBULIBPICYNBBXJXSIXRANNBTVGSNKR

	''.join([up[(up.index(x) + (up.index(cipher[ i % len(cipher) ]))) % 26] for i, x in enumerate(text)])