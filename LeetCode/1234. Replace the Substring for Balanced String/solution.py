from collections import Counter
class Solution:
#     def balancedString(self, s: str) -> int:
#         n = len(s)
#         total = Counter(s)
#         res = n
#         for k in list("QWER"):
#             total[k] -= n//4
#         i = j = 0
#         mp = Counter()
#         def judge():
#             for k in list("QWER"):
#                 if total[k] >= 0:
#                     if mp[k] < total[k]:
#                         return False
#             return True

#         while j < n:
#             mp[s[j]] += 1
#             j += 1
#             while i < n and judge():
#                 res = min(res,j-i)
#                 mp[s[i]] -= 1
#                 i += 1
#         return res
    
    
    def balancedString(self, s):
        count = collections.Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res
