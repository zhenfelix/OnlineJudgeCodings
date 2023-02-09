class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(1,n):
            stones[i] += stones[i-1]
        f = 0
        g = stones[-1]-f
        for i in range(1,n)[::-1]:
            f = g 
            g = max(g, stones[i-1]-f)
        return f 

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        presums = [0]
        for stone in stones:
            presums.append(presums[-1]+stone)
        # if n == 2:
        #     return presums[-1]
        dp = [0]*n
        f = [-float('inf')]*n
        f[-1] = presums[n]-dp[n-1]
        for i in range(n-1)[::-1]:
            dp[i] = f[i+1]
            f[i] = max(f[i+1], presums[i+1]-dp[i])
        # print(presums)
        # print(dp)
        # print(f)
        return dp[0]
