class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        q, ans = 1, 0
        while q <= min(a,b):
            if a%q == 0 and b%q == 0:
                ans += 1
            q += 1
        return ans