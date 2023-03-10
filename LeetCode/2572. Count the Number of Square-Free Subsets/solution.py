primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
mp = dict()
for i in range(2,31):
    s = 0
    x = i 
    for f in primes:
        s <<= 1 
        cnt = 0
        while x%f == 0:
            x //= f 
            cnt += 1
        if cnt > 1:
            s = -1
            break
        elif cnt == 1:
            s |= 1 
    if s > 0:
        mp[i] = s 

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9+7 
        ones = 0
        dp = [0]*(1<<10)
        dp[0] = 1 
        for x in nums:
            if x == 1:
                ones += 1 
            elif x in mp:
                mask = mp[x]
                ndp = dp[:]
                for s in range(1,1<<10):
                    if s&mask == mask:
                        ndp[s] = (dp[s^mask]+ndp[s])%MOD 
                dp = ndp 
        return (pow(2,ones,MOD)*sum(dp)-1)%MOD