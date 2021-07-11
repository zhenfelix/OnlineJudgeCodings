# class Solution:
#     def countPalindromicSubsequence(self, s):
#         res = 0
#         for c in string.ascii_lowercase:
#             i, j = s.find(c), s.rfind(c)
#             if i > -1:
#                 res += len(set(s[i + 1: j]))
#         return res        

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        chars = [chr(x+ord('a')) for x in range(26)]
        left, right = {ch: n for ch in chars}, {ch: -1 for ch in chars}
        res = defaultdict(set)
        for i in range(n):
            right[s[i]] = i  
        for i in range(n)[::-1]:
            left[s[i]] = i 
        for i, ch in enumerate(s):
            for ph in chars:
                if left[ph] < i and right[ph] > i:
                    res[ch].add(ph)
        return sum(len(v) for k, v in res.items())