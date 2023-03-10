class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n:
            if n&1:
                if (n>>1)&1:
                    n += 1
                ans += 1
            n >>= 1
        return ans 