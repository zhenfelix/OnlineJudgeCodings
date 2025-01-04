class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9+7
        ans = m 
        for _ in range(n-1-k):
            ans *= (m-1)
            ans %= MOD
        def quickmul(a,q):
            res = 1  
            while q:
                if q&1:
                    res *= a  
                    res %= MOD
                q >>= 1
                a *= a 
                a %= MOD
            return res 

        b = 1 
        for i in range(1,k+1):
            ans *= (n-i)
            ans %= MOD
            b *= i  
            b %= MOD
        ans *= quickmul(b,MOD-2)
        ans %= MOD
        return ans 
