# from functools import lru_cache
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         @lru_cache(None)
#         def dfs(i):
#             # print(i)
#             if i == n:
#                 return 1
#             if s[i] == "0":
#                 return 0
#             res = 0
#             if s[i] == "*":
#                 res += 9*dfs(i+1)
#             else:
#                 res += dfs(i+1)

#             if i < n-1:
#                 if s[i] == "*" and s[i+1] == "*":
#                     res += 15 * dfs(i+2)
#                 elif s[i] == "*":
#                     res += (2 if s[i+1] <= "6" else 1) * dfs(i+2)
#                 elif s[i+1] == "*":
#                     if int(s[i]) <= 2:
#                         res += [0,9,6][int(s[i])] * dfs(i+2)
#                 else:
#                     res += (1 if int(s[i:i+2]) <= 26 else 0) * dfs(i+2)
#             return res%(10**9+7)
        
#         n = len(s)
#         return dfs(0)


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         a, b = 1, 0
#         state = "*"
#         for ch in s[::-1]:
#             # print(ch,state,a,b)
#             if ch == "0":
#                 a, b = 0, a 
#             elif ch == "*":
#                 if state == "*":
#                     a, b = 9*a+15*b, a 
#                 elif state <= "6":
#                     a, b = 9*a+2*b, a 
#                 else:
#                     a, b = 9*a+b, a 
#             elif state == "*":
#                 if ch == "1":
#                     a, b = a+9*b, a 
#                 elif ch == "2":
#                     a, b = a+6*b, a
#                 else:
#                     a, b = a, a
#             else: 
#                 if int(ch+state) <= 26:
#                     a, b = a+b, a 
#                 else:
#                     a, b = a, a
#             state = ch
#         return a%(10**9+7)



class Solution(object):
    def numDecodings(self, S):
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in S:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0