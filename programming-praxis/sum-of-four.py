import itertools as it

test = [2, 3, 1, 0, -4, -1]
value = 0

# numbers in test can be used more than once: 
# [0, 0, 0, 0] = 0 or [1, 1, -1, -1] = 0
print [i for i in it.combinations_with_replacement(test, 4) if sum(i) == value]

# no numbers in the test array can be used more than once,
# ex: full result set of test = [2, 3, 1, 0, -4, -1] and value = 0:
# [(2, 3, -4, -1), (3, 1, 0, -4)]
print [i for i in it.combinations(test, 4) if sum(i) == value]

# returns all permutations of elements where the sum is equal to the value
# ex: (1, 1, -1, -1), (-1, 1, 1, -1), (-1, 1, -1, 1)
print [i for i in it.product(test, repeat=4) if sum(i) == value]