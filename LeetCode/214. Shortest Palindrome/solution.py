# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n == 0: return ""
#         dp = [n-1]*n
#         cur = 1
#         for i in range(n-2,-1,-1):
#             total = cur
#             cur = 0
#             for idx in range(total):
#                 end = dp[idx]
#                 if end+1 < n and s[i] == s[end+1]:
#                     dp[cur] = end+1
#                     cur += 1
#             if s[i] == s[i+1]:
#                 dp[cur] = i+1
#                 cur += 1
#             dp[cur] = i
#             cur += 1
#         add = s[-1:dp[0]:-1]
#         return add+s

# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
#         rev = s[::-1]
#         n = len(s)
#         for i in range(n-1,-1,-1):
#             if s[:i+1] == rev[n-i-1:]:
#                 return s[-1:i:-1]+s[:]
#         return ""

# class KMP:
#   def findPattern(self, text, pattern):
#       n, m = len(text), len(pattern)
#       next = [-1]*m 
#       i, j = 0, -1
#       while i < m-1:
#           if j == -1 or pattern[i] == pattern[j]:
#               i += 1
#               j += 1
#               next[i] = j
#           else:
#               j = next[j]




#       i, j = 0, 0
#       while i < n and j < m:
#           if j == -1 or text[i] == pattern[j]:
#               i += 1
#               j += 1
#           else:
#               j = next[j]
#       if j == m:
#           return i-m
#       return -1


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def getNext(pattern):
            m = len(pattern)
            i, j = 0, -1
            Next = [-1]*m
            while i < m-1:
                if j == -1 or pattern[i] == pattern[j]:
                    i += 1
                    j += 1
                    Next[i] = j
                else:
                    j = Next[j]
            return Next
        
        Next = getNext(s)
        revs = s[::-1]
        i , j = 0, 0
        n = len(revs)
        while i < n:
            if j == -1 or revs[i] == s[j]:
                i += 1
                j += 1
            else:
                j = Next[j]
        
        return s[-1:j-1:-1]+s