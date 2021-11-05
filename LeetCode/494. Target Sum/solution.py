# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         suffix = nums.copy()
#         for i in range(n-1)[::-1]:
#             suffix[i] += suffix[i+1]
#         @lru_cache(None)
#         def dfs(i, sums):
#             if i == n:
#                 return sums == 0
#             if sums > suffix[i] or sums < -suffix[i]:
#                 return 0
#             return dfs(i+1, sums-nums[i]) + dfs(i+1, sums+nums[i])
#         return dfs(0, target)


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         # nums.sort()
#         n = len(nums)
#         tot = sum(nums)
#         if tot-target < 0 or tot+target < 0 or (tot-target)%2 == 1:
#             return 0
#         dp = [0]*(tot+1)
#         dp[0] = 1
#         for i in range(n):
#             for t in range(tot+1)[::-1]:
#                 if t < nums[i]:
#                     break
#                 dp[t] += dp[t-nums[i]]
#         return dp[(tot-target)//2]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tot = sum(nums)
        if tot-target < 0 or tot+target < 0 or (tot-target)%2 == 1:
            return 0
        target = (tot-target)//2
        dp = [0]*(target+1)
        dp[0] = 1
        for x in nums:
            for t in range(target, x-1, -1):
                dp[t] += dp[t-x]
        return dp[-1]