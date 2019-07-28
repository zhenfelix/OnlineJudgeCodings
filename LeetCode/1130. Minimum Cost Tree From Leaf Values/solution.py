# class Solution:
#     def mctFromLeafValues(self, arr: List[int]) -> int:
#         dp = {}
#         n = len(arr)
#         p = [[0]*n for _ in range(n)]
#         for r in range(n):
#             for c in range(r,n):
#                 if c == r:
#                     p[r][c] = arr[r]
#                 else:
#                     p[r][c] = p[r][c-1]
#                     p[r][c] = max(p[r][c],arr[c])
                        
                    
                    
                    
#         def dfs(i,j):
#             if (i,j) in dp:
#                 return dp[i,j]
#             if i == j:
#                 dp[i,j] = 0
#                 return 0
#             ans = (1<<31)
#             for k in range(i,j):
#                 ans = min(ans,p[i][k]*p[k+1][j]+dfs(i,k)+dfs(k+1,j))
#             dp[i,j] = ans
#             return ans
        
#         return dfs(0,n-1)

class Solution:
    def mctFromLeafValues(self, A):
        res, n = 0, len(A)
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack)  >2:
            res += stack.pop() * stack[-1]
        return res
        