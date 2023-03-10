class Solution:
    def countAnagrams(self, s: str) -> int:
        n = len(s)
        MOD = 10**9+7
        def quickmul(a, q):
            b = 1
            while q:
                if q&1:
                    b = (b*a)%MOD
                a = (a*a)%MOD
                q >>= 1 
            return b 
        fac = [1]*(n+1)
        for i in range(1,n+1):
            fac[i] = (fac[i-1]*i)%MOD 
        ifac = [1]*(n+1)
        ifac[n] = quickmul(fac[n],MOD-2)
        for i in range(n)[::-1]:
            ifac[i] = (ifac[i+1]*(i+1))%MOD
        ans = 1
        for word in s.split():
            cc = Counter(word)
            ans = (ans*fac[len(word)])%MOD 
            for _, v in cc.items():
                ans = (ans*ifac[v])%MOD 
        return ans 