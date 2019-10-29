# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         def dfs(r1,c1,r2,c2):
#             if (r1,c1,r2,c2) in memo:
#                 return memo[r1,c1,r2,c2]
#             if (r1,c1,r2,c2) == (n-1,n-1,n-1,n-1):
#                 memo[r1,c1,r2,c2] = grid[n-1][n-1]
#                 return memo[r1,c1,r2,c2]
#             if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
#                 memo[r1,c1,r2,c2] = -float('inf')
#                 return memo[r1,c1,r2,c2]
#             nxt1 = max(dfs(r1+1,c1,r2,c2),dfs(r1,c1+1,r2,c2))
#             nxt2 = max(dfs(r1,c1,r2+1,c2),dfs(r1,c1,r2,c2+1))
#             if (r1,c1) == (r2,c2):
#                 memo[r1,c1,r2,c2] = max(nxt1,nxt2)
#             else:
#                 memo[r1,c1,r2,c2] = max(nxt1+grid[r1][c1], nxt2+grid[r2][c2])
#             return memo[r1,c1,r2,c2]

#         memo = {}
#         n = len(grid)
#         dfs(0,0,0,0)
#         print(memo)
#         print(memo[2,2,2,2])
#         return max(0,memo[0,0,0,0])


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = collections.defaultdict(int)
        n = len(grid)
        dp[0,n-1,n-1] = grid[n-1][n-1]
        for k in range(1,2*n-1):
            for r1 in range(max(0,n-1-k), min(n-1,2*n-2-k)+1):
                for r2 in range(max(0,n-1-k), min(n-1,2*n-2-k)+1):
                    # print(r1,r2)
                    if grid[r1][2*n-2-k-r1] == -1 or grid[r2][2*n-2-k-r2] == -1:
                        dp[k,r1,r2] = -float('inf')
                        continue
                    cur = grid[r1][2*n-2-k-r1] + grid[r2][2*n-2-k-r2]
                    if r1 == r2:
                        cur //= 2
                    pre = max(dp.get((k-1,r1+1,r2),-float('inf')),dp.get((k-1,r1,r2+1),-float('inf')),
                        dp.get((k-1,r1+1,r2+1),-float('inf')),dp.get((k-1,r1,r2),-float('inf')))
                    dp[k,r1,r2] = cur + pre
        # print(dp)
        return max(0, dp[2*n-2,0,0])