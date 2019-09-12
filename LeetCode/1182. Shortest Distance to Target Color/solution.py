import math

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        left = [[math.inf]*3 for _ in range(n)]
        right = [[math.inf]*3 for _ in range(n)]
        dp = [[math.inf]*3 for _ in range(n)]
        ans = []
        for i in range(n):
            left[i][colors[i]-1] = 0
            right[i][colors[i]-1] = 0
            dp[i][colors[i]-1] = 0
        
        for i in range(1,n):
            for k in range(3):
                left[i][k] = min(left[i][k], left[i-1][k]+1)
        
        for i in range(n-2,-1,-1):
            for k in range(3):
                right[i][k] = min(right[i][k], right[i+1][k]+1)
                
        for i in range(n):
            for k in range(3):
                dp[i][k] = min(left[i][k], right[i][k])
        
        # print(dp)
        for q in queries:
            tmp = dp[q[0]][q[1]-1]
            if tmp == math.inf:
                tmp = -1
            ans.append(tmp)
        return ans