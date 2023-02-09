class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[0,0] for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = dp[0][0][1] = grid[0][0]
        for i in range(1,n):
            dp[i][0][0] = dp[i][0][1] = dp[i-1][0][0]*grid[i][0]
        for j in range(1,m):
            dp[0][j][0] = dp[0][j][1] = dp[0][j-1][0]*grid[0][j]
        for i in range(1,n):
            for j in range(1,m):
                candidates = dp[i-1][j]+dp[i][j-1]
                candidates = [a*grid[i][j] for a in candidates]
                dp[i][j][0] = min(candidates)
                dp[i][j][1] = max(candidates)
        ans = dp[-1][-1][-1]
        MOD = 10**9+7
        return ans%MOD if ans >= 0 else -1

# class Solution:
#     def maxProductPath(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         pos = [[-float('inf')]*m for _ in range(n)]
#         neg = [[float('inf')]*m for _ in range(n)]
#         if grid[0][0] > 0:
#             pos[0][0] = grid[0][0]
#         elif grid[0][0] < 0:
#             neg[0][0] = grid[0][0]
#         else:
#             pos[0][0] = grid[0][0]
#             neg[0][0] = grid[0][0]

#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 0:
#                     pos[i][j], neg[i][j] = 0, 0
#                 elif grid[i][j] > 0:
#                     # pos[i][j] = grid[i][j]
#                     if i-1 >= 0:
#                         pos[i][j] = max(pos[i][j], grid[i][j]*pos[i-1][j])
#                         neg[i][j] = min(neg[i][j], grid[i][j]*neg[i-1][j])
#                     if j-1 >= 0:
#                         pos[i][j] = max(pos[i][j], grid[i][j]*pos[i][j-1])
#                         neg[i][j] = min(neg[i][j], grid[i][j]*neg[i][j-1])
#                 else:
#                     # neg[i][j] = grid[i][j]
#                     if i-1 >= 0:
#                         pos[i][j] = max(pos[i][j], grid[i][j]*neg[i-1][j])
#                         neg[i][j] = min(neg[i][j], grid[i][j]*pos[i-1][j])
#                     if j-1 >= 0:
#                         pos[i][j] = max(pos[i][j], grid[i][j]*neg[i][j-1])
#                         neg[i][j] = min(neg[i][j], grid[i][j]*pos[i][j-1])
#         res = pos[-1][-1]
#         MOD = 10**9+7
#         # print(pos,neg)
#         return res%MOD if res >= 0 else -1


# class Solution:
#     def maxProductPath(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         mx = grid.copy()
#         mi = grid.copy() #NO COPY! WRONG USAGE


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        mx = [[0]*m for _ in range(n)]
        mi = [[0]*m for _ in range(n)]
        mx[0][0] = mi[0][0] = grid[0][0]
        for i in range(1,n):
            mx[i][0] = mi[i][0] = grid[i][0]*mi[i-1][0]
        for j in range(1,m):
            mx[0][j] = mi[0][j] = grid[0][j]*mi[0][j-1]

        for i in range(1,n):
            for j in range(1,m):
                mx_, mi_ = max(mx[i-1][j],mx[i][j-1]), min(mi[i-1][j],mi[i][j-1])
                if grid[i][j] == 0:
                    mx[i][j], mi[i][j] = 0, 0
                elif grid[i][j] > 0:
                    mx[i][j] = mx_*grid[i][j]
                    mi[i][j] = mi_*grid[i][j]
                else:
                    mx[i][j] = mi_*grid[i][j]
                    mi[i][j] = mx_*grid[i][j]
                    
                    
        res = mx[-1][-1]
        MOD = 10**9+7
        return res%MOD if res >= 0 else -1


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def fn(i, j): 
            """Return maximum & minimum products ending at (i, j)."""
            if i == 0 and j == 0: return grid[0][0], grid[0][0]
            if i < 0 or j < 0: return -inf, inf
            if grid[i][j] == 0: return 0, 0
            mx1, mn1 = fn(i-1, j) # from top
            mx2, mn2 = fn(i, j-1) # from left 
            mx, mn = max(mx1, mx2)*grid[i][j], min(mn1, mn2)*grid[i][j]
            return (mx, mn) if grid[i][j] > 0 else (mn, mx)
        
        mx, _ = fn(m-1, n-1)
        return -1 if mx < 0 else mx % 1_000_000_007