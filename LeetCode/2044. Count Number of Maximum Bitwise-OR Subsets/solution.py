class Solution:
    def countMaxOrSubsets(self, A):
        dp = collections.Counter([0])
        for a in A:
            ndp = dp.copy()
            for k, v in dp.items():
                ndp[k | a] += v
            dp = ndp 
        return dp[max(dp)]

# class Solution:
#     def countMaxOrSubsets(self, nums: List[int]) -> int:
#         mx = 0
#         for x in nums:
#             mx |= x
#         n = len(nums)
#         res = 0

#         def dfs(i, cur):
#             nonlocal res
#             if i == n:
#                 res += 1 if cur == mx else 0
#                 return
#             dfs(i+1, cur)
#             dfs(i+1, cur|nums[i])

#         dfs(0,0)
#         return res