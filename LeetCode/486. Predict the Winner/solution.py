# class Solution:
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         def dfs(left,right,first):
#             if (left,right,first) in memo:
#                 return memo[left,right,first]
#             if left > right:
#                 memo[left,right,first] = 0
#                 return 0
#             if first:
#                 memo[left,right,True] = max(nums[left]+dfs(left+1,right,False), nums[right]+dfs(left,right-1,False))
#             else:
#                 memo[left,right,False] = min(-nums[left]+dfs(left+1,right,True, -nums[right]+dfs(left,right-1,True)))
#             return memo[left,right,first]
#         memo = {}
#         return dfs(0,len(nums)-1,True) >= 0


# class Solution:
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         def winner(left,right):
#             if (left,right) in memo:
#                 return memo[left,right]
#             if left == right:
#                 memo[left,right] = nums[left]
#                 return nums[left]
#             a, b = nums[left] - winner(left+1,right), nums[right] - winner(left,right-1)
#             memo[left,right] = max(a,b)
#             return memo[left,right]
#         memo = {}
#         return winner(0,len(nums)-1) >= 0


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = nums.copy()
        n = len(nums)
        for d in range(1,n):
            # print(dp)
            for start in range(n-d):
                dp[start] = max(nums[start+d]-dp[start],nums[start]-dp[start+1])
        return dp[0] >= 0