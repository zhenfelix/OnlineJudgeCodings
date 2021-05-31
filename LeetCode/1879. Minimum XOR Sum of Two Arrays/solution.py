from functools import lru_cache
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        @lru_cache(None)
        def dfs(idx, remains):
            if idx == n or remains == 0:
                return 0
            return min((nums1[idx]^nums2[i]) + dfs(idx+1,remains-(1<<i)) for i in range(n) if remains&(1<<i))
        return dfs(0, (1<<n)-1)


class Solution:
    def minimumXORSum(self, a: List[int], b: List[int]) -> int:
        @lru_cache(None)
        def dp(mask: int) -> int:
            i = bin(mask).count("1")
            if i >= len(a):
                return 0
            return min((a[i] ^ b[j]) + dp(mask + (1 << j)) 
                       for j in range(len(b)) if mask & (1 << j) == 0)
        return dp(0