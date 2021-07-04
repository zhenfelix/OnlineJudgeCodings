class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even, odd = n//2+(n&1), n//2
        return (pow(5,even,MOD)*pow(4,odd,MOD))%MOD