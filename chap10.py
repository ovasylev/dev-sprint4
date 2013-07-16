# ---------Ex. 10.7-----------

def letters_count(word):
	alphabet = [0] * (ord('z') - ord('a') + 1)
	for letter in word:
		base = ord('a')
		pos = ord(letter) - base
		alphabet[pos] += 1
	return alphabet

def is_anagram(word1, word2):
	word_list1 = letters_count(word1)
	word_list2 = letters_count(word2)
	if len(word_list1) != len(word_list2):
		return False
	else:
		for i in range(len(word_list1)):
			if word_list2[i] != word_list1[i]:
				return False
		return True


print is_anagram('bakal', 'kabla')
# Result: True
print is_anagram('bakal', 'kabls')
# Result: False
print is_anagram('bakal', 'bcdfg')
# Result: False