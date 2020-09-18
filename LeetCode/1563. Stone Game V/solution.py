class Solution:
    def stoneGameV(self, A):
        n = len(A)
        prefix = [0] * (n + 1)
        for i, a in enumerate(A):
            prefix[i + 1] = prefix[i] + A[i]

        @functools.lru_cache(None)
        def dp(i, j):
            if i == j: return 0
            res = 0
            for m in range(i, j):
                left = prefix[m + 1] - prefix[i]
                right = prefix[j + 1] - prefix[m + 1]
                if left <= right:
                    res = max(res, dp(i, m) + left)
                if left >= right:
                    res = max(res, dp(m + 1, j) + right)
            return res
        return dp(0, n - 1)        
    

    # @szzzwno123 sad... It takes 1200ms on my side. The reason why top-down solution is faster is that the top-down solution will never touch the segment that has a bigger sum than the other one.


class Solution:
    def stoneGameV(self, A):
        n = len(A)
        m = n + 1
        f, g, s = [[0]*m for _ in range(m)], [[0]*m for _ in range(m)], [[0]*m for _ in range(m)]
        mxl, mxr = [[0]*m for _ in range(m)], [[0]*m for _ in range(m)]
        for i in range(n):
            g[i][i] = i 
            s[i][i] = A[i]
            for j in range(i+1,n):
                s[i][j] = s[i][j-1] + A[j]
                now = g[i][j-1]
                while s[i][now] < s[i][j] - s[i][now]:
                    now += 1
                g[i][j] = now

        for sz in range(1,n+1):
            i = 0
            while i+sz-1 < n:
                j = i+sz-1
                mid = g[i][j]
                left, right = s[i][mid], s[mid+1][j]
                if left == right:
                    f[i][j] = max(f[i][j], mxl[i][mid])
                    f[i][j] = max(f[i][j], mxr[mid+1][j])
                else:
                    if mid > i:
                        f[i][j] = max(f[i][j], mxl[i][mid-1])
                    if mid < j:
                        f[i][j] = max(f[i][j], mxr[mid+1][j])
                v = f[i][j] + s[i][j]
                if i == j:
                    mxr[i][j] = mxl[i][j] = v
                else:
                    mxl[i][j] = max(mxl[i][j-1], v)
                    mxr[i][j] = max(mxr[i+1][j], v)
                i += 1
        return f[0][n-1]


