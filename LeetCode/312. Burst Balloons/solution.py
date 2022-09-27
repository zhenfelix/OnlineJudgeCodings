class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        @cache
        def dfs(i,j):
            if i+1 >= j:
                return 0
            return max(nums[i]*nums[k]*nums[j]+dfs(i,k)+dfs(k,j) for k in range(i+1,j))
        return dfs(-1,n)


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



# for given interval [i,j], assume we have the solution operation sequece ...ij...k, where k is the last operation and j is the most close operation next to i, if i and j are one different side of k, we can exchange i and j without worsening our solution
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        @lru_cache(None)
        def dfs(i,j):
            if i > j:
                return 0
            return max(nums[k]*nums[i-1]*nums[j+1]+dfs(i,k-1)+dfs(k+1,j) for k in range(i,j+1))
        return dfs(0,n-1)