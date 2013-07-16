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

#------------Ex.11.10--------------

def move_letter(letter, index):
	start_pos = ord(letter)
	end_pos = start_pos + index
	if end_pos < 97:
		end_pos = 123 - (97 - end_pos)
	elif end_pos > 122:
		end_pos = 97 + (end_pos - 123)
	new_letter = chr(end_pos)
	return new_letter

def rotate_word(word, index):
	new_word = ''
	for i in range(len(word)):
		new_word += move_letter(word[i], index)
	return new_word

def rotate_pairs(file, index):
	temp_pairs = dict()
	pairs = dict()
	fin = open(file, 'r+')
	for line in fin:
		word = line.strip()
		new_word = rotate_word(word, index)
		fo = open(file, 'r+')
		for l in fo:
			if new_word == l.strip():
				pairs[word] = new_word
	return pairs
		
print rotate_pairs('data.txt', 2)
