# class Solution:
#     def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
#         n, INF = len(nums), 200 * 1e6

#         @lru_cache(None)
#         def dp(i, k):
#             if i == n: return 0
#             if k == -1: return INF
#             ans = INF
#             maxNum = nums[i]
#             totalSum = 0
#             for j in range(i, n):
#                 maxNum = max(maxNum, nums[j])
#                 totalSum += nums[j]
#                 wasted = maxNum * (j - i + 1) - totalSum
#                 ans = min(ans, dp(j + 1, k - 1) + wasted)
#             return ans

#         return dp(0, k)


from functools import lru_cache
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], K: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def dfs(i,k):
            if n-i <= k+1:
                return 0
            if k == -1:
                return float('inf')
            res = float('inf')
            mx, sums = 0, 0
            for j in range(i,n):
                mx = max(mx, nums[j])
                sums += nums[j]
                res = min(res, mx*(j+1-i)-sums+dfs(j+1,k-1))
            return res 
        return dfs(0,K)