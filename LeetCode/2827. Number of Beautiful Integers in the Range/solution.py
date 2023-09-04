class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        low, high = str(low), str(high)
        n = len(high)
        low = '0'*(n-len(low))+low 
        @lru_cache(None)
        def dfs(flo,fhi,r,odd,even,i):
            if i == n:
                return odd == even and r%k == 0
            lo = int(low[i]) if flo else 0
            hi = int(high[i]) if fhi else 9
            ans = 0 
            for ch in range(lo,hi+1):
                fodd, feven = 0, 0 
                if odd > 0 or even > 0 or ch > 0:
                    if ch%2 == 1:
                        fodd = 1
                    else:
                        feven = 1
                # ans += dfs(flo and ch == lo, fhi and ch == hi, (r+ch*(10**(n-i-1)))%k, odd+fodd, even+feven, i+1)
                ans += dfs(flo and ch == lo, fhi and ch == hi, (r*10+ch)%k, odd+fodd, even+feven, i+1)
            # print(flo,fhi,r,odd,even,i,ans)
            return ans 
        return dfs(1,1,0,0,0,0)

