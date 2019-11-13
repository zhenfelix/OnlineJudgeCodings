# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         nums = [1]+nums+[1]
#         n = len(nums)
#         def dfs(left, right):
#             if (left,right) in memo:
#                 return memo[left,right]
#             if left+1 == right:
#                 memo[left,right] = 0
#                 return memo[left,right]
#             memo[left,right] = max([nums[left]*nums[k]*nums[right]+dfs(left,k)+dfs(k,right) for k in range(left+1,right)])
#             return memo[left,right]
#         memo = {}
#         return dfs(0,len(nums)-1)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for sz in range(3,n+1):
            for left in range(0,n-sz+1):
                right = left+sz-1
                dp[left][right] = max([nums[left]*nums[k]*nums[right]+dp[left][k]+dp[k][right] for k in range(left+1,right)])
        return dp[0][n-1]