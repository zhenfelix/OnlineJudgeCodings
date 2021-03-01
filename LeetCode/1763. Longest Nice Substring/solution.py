class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: return "" # boundary condition 
        ss = set(s)
        candidates = []
        pre = 0
        for i, c in enumerate(s):
            if c.swapcase() not in ss: 
                candidates.append(self.longestNiceSubstring(s[pre:i]))
                pre = i+1
        if len(candidates) == 0:
            return s 
        candidates.append(self.longestNiceSubstring(s[pre:]))
        return max(*candidates, key=len)


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: return "" # boundary condition 
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss: 
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s

# class Solution:
#     def longestNiceSubstring(self, s: str) -> str:
#         n, res = len(s), [0,-1]
        
#         def pair(ch):
#             delta = ord('A') - ord('a')
#             if 'A' <= ch <= 'Z':
#                 delta = -delta
#             return chr(ord(ch)+delta)

#         for i in range(n):
#             unbalanced, balanced = set(), set()
#             for j in range(i,n):
#                 if pair(s[j]) in unbalanced:
#                     unbalanced.remove(pair(s[j]))
#                     balanced.add(s[j])
#                     balanced.add(pair(s[j]))
#                 elif s[j] not in balanced:
#                     unbalanced.add(s[j])
#                 if not unbalanced and j-i > res[-1]-res[0]:
#                     res = [i,j]
#                 # print(i,j,unbalanced,balanced)
#         return s[res[0]:res[-1]+1]


# class Solution:
#     def valid(self, s):
#         st = set(s)
#         for ch in st:
#             delta = ord('A')-ord('a')
#             if 'A' <= ch <= 'Z':
#                 delta = -delta
#             if chr(ord(ch)+delta) not in st:
#                 return False
#         return True


#     def longestNiceSubstring(self, s: str) -> str:
#         res, n = "", len(s)
#         for i in range(n):
#             for j in range(i,n):
#                 if self.valid(s[i:j+1]) and j-i+1 > len(res):
#                     res = s[i:j+1]
#         return res 