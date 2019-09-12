# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if len(p) == 0:
#             return len(s) == 0
#         if len(s) == 0:
#             return p[0] == '*' and self.isMatch("", p[1:])
#         if p[0] == '*':
#             return self.isMatch(s[1:], p[:]) or self.isMatch(s[:], p[1:])
#         if p[0] == '?':
#             return self.isMatch(s[1:], p[1:])
#         return s[0] == p[0] and self.isMatch(s[1:], p[1:])
    
    
    
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         n, m = len(s), len(p)
#         dp = {}
#         def dfs(i, j):
#             if (i,j) in dp:
#                 return dp[i,j]
#             if j == m:
#                 dp[i,j] = (i == n)
#                 return dp[i,j]
#             if i == n:
#                 dp[i,j] = (p[j] == '*' and dfs(i,j+1))
#                 return dp[i,j]
#             if p[j] == '*':
#                 dp[i,j] = (dfs(i+1,j) or dfs(i,j+1))
#                 return dp[i,j]
#             if p[j] == '?':
#                 dp[i,j] = dfs(i+1,j+1)
#                 return dp[i,j]
#             dp[i,j] = (s[i] == p[j] and dfs(i+1,j+1))
#             return dp[i,j]
#         return dfs(0,0)


# The original post has DP 2d array index from high to low, which is not quite intuitive.

# Below is another 2D dp solution. Ideal is identical.

# dp[i][j] denotes whether s[0....i-1] matches p[0.....j-1],

# First, we need to initialize dp[i][0], i= [1,m]. All the dp[i][0] should be false because p has nothing in it.

# Then, initialize dp[0][j], j = [1, n]. In this case, s has nothing, to get dp[0][j] = true, p must be '*', '**', '***',etc. Once p.charAt(j-1) != '*', all the dp[0][j] afterwards will be false.

# Then start the typical DP loop.

# Though this solution is clear and easy to understand. It is not good enough in the interview. it takes O(mn) time and O(mn) space.

# Improvement: 1) optimize 2d dp to 1d dp, this will save space, reduce space complexity to O(N). 2) use iterative 2-pointer.


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         n, m = len(s), len(p)
#         dp = [[False]*(m+1) for _ in range(n+1)]
#         dp[0][0] = True
#         for i in range(1,n+1):
#             dp[i][0] = False
#         for j in range(1,m+1):
#             if p[j-1] == '*':
#                 dp[0][j] = True
#             else:
#                 break
#         for i in range(1,n+1):
#             for j in range(1,m+1):
#                 if p[j-1] != '*':
#                     dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == '?')
#                 else:
#                     dp[i][j] = dp[i-1][j] or dp[i][j-1]
#         return dp[n][m]



# https://leetcode.com/problems/wildcard-matching/discuss/138878/Finite-state-machine-with-Python-and-dictionary.-13-lines-O(p+s)-time?page=1
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        transfer = {}
        state = 0
        
        for char in p:
            if char == '*':
                transfer[state, char] = state
            else:
                transfer[state, char] = state + 1
                state += 1
        
        accept = state
        state = set([0])
        
        for char in s:
            state = set([transfer.get((at, token)) for at in state for token in [char, '*', '?']])
        
        return accept in state