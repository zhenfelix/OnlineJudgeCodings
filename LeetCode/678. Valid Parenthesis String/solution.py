
class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt = 0
        for ch in s:
            if ch == '(' or ch == '*':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                return False
        cnt = 0
        for ch in s[::-1]:
            if ch == ')' or ch == '*':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                return False
        return True

class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        for ch in s:
            if ch == "(":
                lo += 1
                hi += 1
            elif ch == ")":
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
            lo = max(lo, 0)
            if hi < 0:
                return False
        return lo == 0
       
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo -= 1
                hi -= 1
            else:
                hi += 1
                if lo > 0:
                    lo -= 1
            if lo < 0:
                lo = 0
            if hi < 0:
                return False
        return lo == 0

# class Solution(object):
#     def checkValidString(self, s):
#         if not s: return True
#         LEFTY, RIGHTY = '(*', ')*'

#         n = len(s)
#         dp = [[False] * n for _ in s]
#         for i in range(n):
#             if s[i] == '*':
#                 dp[i][i] = True
#             if i < n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
#                 dp[i][i+1] = True

#         for size in range(2, n):
#             for i in range(n - size):
#                 if s[i] == '*' and dp[i+1][i+size]:
#                     dp[i][i+size] = True
#                 elif s[i] in LEFTY:
#                     for k in range(i+1, i+size+1):
#                         if (s[k] in RIGHTY and
#                                 (k == i+1 or dp[i+1][k-1]) and
#                                 (k == i+size or dp[k+1][i+size])):
#                             dp[i][i+size] = True

#         return dp[0][-1]
#        


# - [two pass greedy approach](https://leetcode.com/problems/valid-parenthesis-string/discuss/453852/two-pass-greedy-approach)
# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         left, star_left = 0, 0
#         for ch in s:
#             # print(ch, left, star)
#             if ch == "(":
#                 left += 1
#             elif ch == "*":
#                 star_left += 1
#             else:
#                 if left > 0:
#                     left -= 1
#                 elif star_left > 0:
#                     star_left -= 1
#                 else:
#                     return False
#         right, star_right = 0, 0
#         for ch in s[::-1]:
#             # print(ch, left, star)
#             if ch == ")":
#                 right += 1
#             elif ch == "*":
#                 star_right += 1
#             else:
#                 if right > 0:
#                     right -= 1
#                 elif star_right > 0:
#                     star_right -= 1
#                 else:
#                     return False
#         # return left <= star_left and right <= star_right
#         return True


# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         st = []
#         right, star = 0, 0
#         for ch in s:
#             if ch != ")":
#                 st.append(ch)
#             elif not st:
#                 return False
#             elif st and st[-1] == "(":
#                 st.pop()
#             else:
#                 st.append(ch)
                    
#         while st:
#             ch = st.pop()
#             if ch == ")":
#                 right += 1
#             elif ch == "*":
#                 star += 1
#             elif right > 0:
#                 right -= 1
#             elif star > 0:
#                 star -= 1
#             else:
#                 return False
#         return star >= right