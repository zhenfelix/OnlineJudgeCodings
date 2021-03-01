class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])

        def dfs(r,c):
            if (r,c) in memo:
                return memo[r,c]
            memo[r,c] = 0
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0 <= r+dr < n and 0 <= c+dc < m and matrix[r][c] > matrix[r+dr][c+dc]:
                    memo[r,c] = max(memo[r,c], dfs(r+dr, c+dc))
            memo[r,c] += 1
            return memo[r,c]

        memo = {}
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i,j))
        return res


# longest path in DAG