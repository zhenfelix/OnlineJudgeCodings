class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        if k == n*n:
            return 1
        cb = [[1]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,i):
                cb[i][j] = cb[i-1][j] + cb[i-1][j-1]

        cnt = 0
        # print(cb)
        for r in range(n):
            for c in range(n):
                if n*(r+c) - r*c == k:
                    # print(r,c)
                    cnt += cb[n][r]*cb[n][c]
        return cnt
