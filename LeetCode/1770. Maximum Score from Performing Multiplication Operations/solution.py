# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#         n, m = len(nums), len(multipliers)
#         @lru_cache(None)
#         def dfs(i,j):
#             if i == m:
#                 return 0
#             res = max(multipliers[i]*nums[j]+dfs(i+1,j+1),multipliers[i]*nums[j-i-1]+dfs(i+1,j))
#             # print(i,j,res)
#             return res
#         ans = dfs(0,0)
#         dfs.cache_clear()
#         return ans
    
    
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [0]*(m+1)
        for i in range(m)[::-1]:
            for j in range(i+1):
                dp[j] = max(dp[j]+multipliers[i]*nums[j-i-1], dp[j+1]+multipliers[i]*nums[j])
        return dp[0]