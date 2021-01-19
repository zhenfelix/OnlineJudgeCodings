class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n+1)]
        res = 0
        for i in range(n):
            arr = []
            for j in range(m):
                if matrix[i][j]:
                    dp[i][j] = dp[i-1][j] + matrix[i][j]
                arr.append(dp[i][j])
            arr = sorted(arr, key=lambda x: -x)
            # print(arr)
            h = float('inf')
            for j in range(m):
                h = min(h,arr[j])
                res = max(res,(j+1)*h)
        # print(dp)
        return res 