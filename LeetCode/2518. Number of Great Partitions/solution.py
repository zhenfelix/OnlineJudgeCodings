class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7 
        g = [0]*(k+1)
        f = [1]*(k+1)
        g[0] = 1
        for x in nums:
            for i in range(1,k+1)[::-1]:
                if i-x >= 0:
                    g[i] = (g[i]+g[i-x])
                    f[i] = (f[i]+f[i-x])
                else:
                    g[i] = (g[i]+g[0])
            g[0] = g[1]+1
                    
            # print(x,g,f)
        return max(0,g[k]-f[k-1])%MOD

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # if sum(nums) < 2 * k: return 0
        MOD = 10**9+7 
        f = [1]*(k+1)
        n = len(nums)
        for x in nums:
            for i in range(1,k+1)[::-1]:
                if i-x >= 0:
                    f[i] = (f[i]+f[i-x])

        return max(0,pow(2,n)-f[k-1]*2)%MOD