# class Solution(object):
#     def isMatch(self, text, pattern):
#         if not pattern:
#             return not text

#         first_match = bool(text) and pattern[0] in {text[0], '.'}

#         if len(pattern) >= 2 and pattern[1] == '*':
#             return (self.isMatch(text, pattern[2:]) or
#                     first_match and self.isMatch(text[1:], pattern))
#         else:
#             return first_match and self.isMatch(text[1:], pattern[1:])
        

        
class Solution(object):
    def isMatch(self, text, pattern):
        dp = {}
        def dfs(i,j):
            if not pattern[j:]:
                return not text[i:]
            if (i,j) in dp:
                return dp[i,j]
            first_match = bool(text[i:]) and pattern[j] in {text[i], '.'}
            
            if len(pattern[j:]) >= 2 and pattern[j+1] == '*':
                dp[i,j] = dfs(i,j+2) or (first_match and dfs(i+1,j))
                return dp[i,j]
            else:
                dp[i,j] = first_match and dfs(i+1,j+1)
                return dp[i,j]

        return dfs(0,0)


# class Solution(object):
#     def isMatch(self, text, pattern):
#         dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

#         dp[-1][-1] = True
#         for i in range(len(text), -1, -1):
#             for j in range(len(pattern) - 1, -1, -1):
#                 first_match = i < len(text) and pattern[j] in {text[i], '.'}
#                 if j+1 < len(pattern) and pattern[j+1] == '*':
#                     dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
#                 else:
#                     dp[i][j] = first_match and dp[i+1][j+1]

#         return dp[0][0]