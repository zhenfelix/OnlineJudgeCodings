class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        MOD = 10**9+7
        pow2 = [1]*n  
        for i in range(1,n):
            pow2[i] = 2*pow2[i-1]
            pow2[i] %= MOD
        fac = [1]*(n+1)
        for i in range(1,n+1):
            fac[i] = fac[i-1]*i  
            fac[i] %= MOD
        ans = 1
        m = len(sick)
        arr = []
        cnt = 0
        for i in range(1,m):
            v = sick[i]-sick[i-1]-1
            arr.append(v)
            cnt += max(v-1,0)
            # ans = ans*pow2[max(v-1,0)]
            # ans %= MOD 
        # print(ans)
        ans = ans*pow2[cnt]
        arr.append(sick[0])
        arr.append(n-sick[-1]-1)
        tot = sum(arr)
        # print(arr,tot)
        ans = ans*fac[tot]
        ans %= MOD 
        de = 1
        for a in arr:
            de = de*fac[a]
            de %= MOD  
        return ans*pow(de,-1,MOD)%MOD