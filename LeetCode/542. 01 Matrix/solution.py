class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        dp = [[float('inf')]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                if i:
                    dp[i][j] = min(dp[i][j],dp[i-1][j]+1)
                if j:
                    dp[i][j] = min(dp[i][j],dp[i][j-1]+1)

        for i in range(n)[::-1]:
            for j in range(m)[::-1]:
                if i < n-1:
                    dp[i][j] = min(dp[i][j],dp[i+1][j]+1)
                if j < m-1:
                    dp[i][j] = min(dp[i][j],dp[i][j+1]+1)
        return dp 



    def updateMatrix(self, A):
        R, C = len(A), len(A[0])
        def neighbors(r, c):
            for cr, cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc
                    
        q = collections.deque([((r, c), 0) 
                for r in xrange(R) 
                for c in xrange(C) 
                if A[r][c] == 0])
        seen = {x for x,_ in q}
        ans = [[0]*C for _ in A]
        while q:
            (r, c), depth = q.popleft()
            ans[r][c] = depth
            for nei in neighbors(r, c):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, depth + 1))
        
        return ans