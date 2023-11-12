class Solution:
    def stringCount(self, n: int) -> int:
        mod = 1_000_000_007
        def f1(s):
            return pow(s, n, mod)
        def f2(s):
            return n*pow(s-1, n-1, mod) + pow(s-1, n, mod)
        return (f1(26) - 2*f1(25) - f2(26) + 2*f2(25) + f1(24) - f2(24)) % mod;

作者：newhar
链接：https://leetcode.cn/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10**9+7
        leet,lee,eet,let, le,ee,et,lt, l,e,t,null=0,0,0,0, 0,0,0,0, 0,0,0,1
        for _ in range(n):
            leet = (lee+eet+let+leet*23)%MOD
            lee = (le+ee+lee*24)%MOD
            eet = (ee+et+eet*24)%MOD
            let = (le+et+lt+let*23)%MOD
            le = (l+e+le*24)%MOD
            ee = (e+ee*25)%MOD 
            et = (e+t+et*24)%MOD
            lt = (l+t+lt*24)%MOD
            l = (null+l*25)%MOD
            e = (null+e*25)%MOD
            t = (null+t*25)%MOD
            null = (null*26)%MOD
        return leet


import numpy as np

class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10**9+7
        mat = np.zeros((12,12), dtype = int)
        for s in range(12)[::-1]:
            cnt = 0
            tmp = s  
            base = 1
            if tmp%2:
                cnt += 1
                mat[s,s-base] = 1
            tmp //= 2
            base *= 2 
            if tmp%2:
                cnt += 1
                mat[s,s-base] = 1
            tmp //= 2
            base *= 2
            if tmp%3:
                cnt += 1
                mat[s,s-base] = 1
            mat[s,s] = 26-cnt
        dp = [0]*12
        dp[0] = 1
        dp = np.array(dp)
        # for _ in range(n):
        #     dp = mat@dp
        #     dp %= MOD
        while n:
            if n&1:
                dp = mat@dp 
                dp %= MOD
            n >>= 1
            mat = mat@mat
            mat %= MOD 
        return int(dp[-1])
