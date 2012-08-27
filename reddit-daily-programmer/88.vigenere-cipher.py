# Challenge: http://www.reddit.com/r/dailyprogrammer/comments/y5sox/8132012_challenge_88_easy_vigen%C3%A8re_cipher/
# Solution: http://www.reddit.com/r/dailyprogrammer/comments/y5sox/8132012_challenge_88_easy_vigen%C3%A8re_cipher/c5socop
# by @dvoiss on github / @daveasaurus on reddit

from string import ascii_uppercase as up

def encode(text, cipher, decode=False):
	result, cipher_index, decode = '', 0, -1 if decode else 1
	for i, x in enumerate(text):
		result += up[(up.index(x) + (decode * up.index(cipher[cipher_index % len(cipher) ]))) % 26]
		cipher_index += 1
	return result

print encode("THECAKEISALIE", "GLADOS", False)
print encode("ZSEFOCKTSDZAK", "GLADOS", True)

# HSULAREFOTXNMYNJOUZWYILGPRYZQVBBZABLBWHMFGWFVPMYWAVVTYISCIZRLVGOPGBRAKLUGJUZGLNBASTUQAGAVDZIGZFFWVLZSAZRGPVXUCUZBYLRXZSAZRYIHMIMTOJBZFZDEYMFPMAGSMUGBHUVYTSABBAISKXVUCAQABLDETIFGICRVWEWHSWECBVJMQGPRIBYYMBSAPOFRIMOLBUXFIIMAGCEOFWOXHAKUZISYMAHUOKSWOVGBULIBPICYNBBXJXSIXRANNBTVGSNKR

# one-liner:
''.join([up[(up.index(x) + (up.index(cipher[ i % len(cipher) ]))) % 26] for i, x in enumerate(text)])