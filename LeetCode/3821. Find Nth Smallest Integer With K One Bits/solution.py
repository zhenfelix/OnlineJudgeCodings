class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        ans = 0
        for i in range(49, -1, -1):
            c = math.comb(i, k)
            if n > c:
                ans |= 1 << i
                n -= c
                k -= 1
        return ans