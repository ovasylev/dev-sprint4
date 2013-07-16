#--------Ex. 11.9-------------

def freq(s):
	d = dict()
	for letter in s:
		if letter not in d:
			d[letter] = 1
		else:
			d[letter] += 1
	return d

def has_duplicates(s):
	d = freq(s)
	vals = d.values()
	for i in range(len(vals)):
		if vals[i] > 1:
			return True
	return False


print has_duplicates('abcdefff')
'''
Result: 
{'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'f': 3}
[1, 1, 1, 1, 1, 3]
True
'''

print has_duplicates('abc')
'''
Result:
{'a': 1, 'c': 1, 'b': 1}
[1, 1, 1]
False
'''

print has_duplicates('ababagalamaga')
'''
Result:
{'a': 7, 'b': 2, 'm': 1, 'l': 1, 'g': 2}
[7, 2, 1, 1, 2]
True
'''