class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9+7
        def quick(a,q):
            ans = 1
            while q:
                if q&1:
                    ans = (ans*a)%MOD
                q >>= 1
                a = (a*a)%MOD
            return ans 
        return (quick(2,n)-2+MOD)%MOD