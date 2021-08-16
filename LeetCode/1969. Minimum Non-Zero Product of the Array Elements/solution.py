class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        MOD = 10**9+7
        mx = pow(2,p)-1
        a = mx - 1
        return mx*pow(a,a//2,MOD)%MOD