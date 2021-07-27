class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        dp = points[0][:]
        for i in range(1,n):
            leftmx, right = -1, []
            ndp = []
            for j in range(m):
                while right and dp[right[-1]]-right[-1] <= dp[j]-j:
                    right.pop()
                right.append(j)
            right = right[::-1]
            for j in range(m):
                if leftmx == -1 or dp[leftmx]+leftmx <= dp[j]+j:
                    leftmx = j  
                while right and right[-1] < j:
                    right.pop()
                ndp.append(max(dp[leftmx]+leftmx-j,dp[right[-1]]-right[-1]+j)+points[i][j])
            dp = ndp
            # print(dp)
        return max(dp)
