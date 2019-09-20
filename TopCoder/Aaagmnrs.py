# Problem Statement
# Two phrases are anagrams if they are permutations of each other, ignoring spaces and capitalization. For example, "Aaagmnrs" is an anagram of "anagrams", and "TopCoder" is an anagram of "Drop Cote". Given a phrases, remove each phrase that is an anagram of an earlier phrase, and return the remaining phrases in their original order.

# Definition
# Class: Aaagmnrs
# Method: anagrams
# Parameters: string[]
# Returns: string[]
# Method signature: string[] anagrams(string[] phrases)
# (be sure your method is public)
# Limits
# Time limit (s): 840.000
# Memory limit (MB): 64
# Constraints
# - phrases contains between 2 and 50 elements, inclusive.
# - Each element of phrases contains between 1 and 50 characters, inclusive.
# - Each element of phrases contains letters ('a'-'z' and 'A'-'Z') and spaces (' ') only.
# - Each element of phrases contains at least one letter.
# Examples
# 0)
# { "Aaagmnrs", "TopCoder", "anagrams", "Drop Cote" }
# Returns: { "Aaagmnrs", "TopCoder" }
# The examples above.
# 1)
# { "SnapDragon vs tomek", "savants groped monk", "Adam vents prongs ok" }
# Returns: { "SnapDragon vs tomek" }
# 2)
# { "Radar ghost jilts Kim", "patched hers first", "DEPTH FIRST SEARCH", "DIJKSTRAS ALGORITHM" }
# Returns: { "Radar ghost jilts Kim", "patched hers first" }


from collections import Counter

class Aaagmnrs:
	def anagrams(self, strs):
		mp = set()
		alphabet = [chr(ord('a')+i) for i in range(26)]
		res = []
		for string in strs:
			tmp = ''
			cnt = Counter((string.lower()))
			for ch in alphabet:
				tmp += ch*cnt[ch]
			if tmp not in mp:
				mp.add(tmp)
				res.append(string)
		return res