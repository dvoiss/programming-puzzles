# Challenge: http://www.reddit.com/r/dailyprogrammer/comments/yqxyy/8242012_challenge_91_intermediate_cantors/
# Solution: http://www.reddit.com/r/dailyprogrammer/comments/yqxyy/8242012_challenge_91_intermediate_cantors/c5zd21p
# run code at http://ideone.com/C9xc2
# by @dvoiss on github / @daveasaurus on reddit

def cantor(): 
	i = 1
	while True:
		for j in range(1, i + 1):
			if i % 2 == 0: yield (i - j + 1) / float(j)
			else: yield j / float(i - j + 1)
		i += 1

generator = cantor()
results = []
while len(results) <= 1000:
	item = generator.next()
	if item not in results:
		results.append(item)
		print item