# class Solution:
#     def minSteps(self, s: str, t: str) -> int:
#         s = Counter(s)
#         t = Counter(t)
#         cnt = 0
#         for i in range(26):
#             ch = chr(ord('a')+i)
#             if s[ch] > t[ch]:
#                 cnt += s[ch]-t[ch]
#         return cnt

class Solution:
	def minSteps(self, s: str, t: str) -> int:
		res = 0
		s = collections.Counter(s)
		t = collections.Counter(t)
		for c in string.ascii_lowercase:
			res += s[c] - t[c] if s[c] > t[c] else 0
		return res