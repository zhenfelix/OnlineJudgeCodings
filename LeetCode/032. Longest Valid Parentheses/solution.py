# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#         ans = 0
#         dp = [0]*n
#         for i, ss in enumerate(s):
#             if i >= 1 and i-1-dp[i-1] >= 0 and ss == ')' and s[i-1-dp[i-1]] == '(':
#                 dp[i] = dp[i-1] + 2
#                 # print(i, dp[i])
#                 if i-2-dp[i-1] >= 0:
#                     # print(i-2-dp[i-1], "exist")
#                     dp[i] += dp[i-2-dp[i-1]]
#                 ans = max(ans, dp[i])
#         # print(dp)
#         return ans 


# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         n = len(s)
#         if n < 2:
#             return 0
#         dp = [0]*n 
#         if s[:2] == '()':
#             dp[1] = 2
#         res = max(dp)
#         for i in range(2,n):
#             if s[i] == ')':
#                 if s[i-1] == '(':
#                     dp[i] = dp[i-2] + 2
#                 elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
#                     dp[i] = dp[i-1] + 2
#                     if i-dp[i-1]-2 >= 0:
#                         dp[i] += dp[i-dp[i-1]-2]
#             res = max(res,dp[i])
#         # print(dp)
#         return res

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        res = 0
        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)
            elif ch == ')' and st and s[st[-1]] == '(':
                st.pop()
                if st:
                    res = max(res, i-st[-1])
                else:
                    res = max(res, i+1)
            else:
                st.append(i)
        return res