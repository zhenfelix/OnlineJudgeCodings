# https://www.bilibili.com/video/BV1zN4y1K762

class Solution:
    def unSuitability(self, operate: List[int]) -> int:
        mx = max(operate)*2
        n = len(operate)
        dp = [float('inf')]*(mx+1)
        dp[0] = 0
        for a in operate:
            ndp = [float('inf')]*(mx+1)
            for j in range(mx+1):
                if j+a <= mx:
                    ndp[j+a] = min(ndp[j+a], max(dp[j], j+a))
                if j-a >= 0:
                    ndp[j-a] = min(ndp[j-a], dp[j])
                else:
                    ndp[0] = min(ndp[0], dp[j]-j+a)
            dp = ndp
        return min(dp)