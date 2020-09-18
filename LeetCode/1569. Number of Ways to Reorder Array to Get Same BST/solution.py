class Solution:
    # def numOfWays(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     node = [[-1,-1] for _ in range(n+1)]
    #     MOD = 10**9 + 7
    #     def insert(x, cur):
    #         if x == cur:
    #             return
    #         if x > cur:
    #             if node[cur][-1] == -1:
    #                 node[cur][-1] = x
    #             insert(x, node[cur][-1])
    #         else:
    #             if node[cur][0] == -1:
    #                 node[cur][0] = x
    #             insert(x, node[cur][0])
    #         return
    #     for num in nums:
    #         insert(num, nums[0])
    #     dp = [[1]*(n+1) for _ in range(n+1)]
    #     for i in range(1,n+1):
    #         for j in range(1,i):
    #             dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    #             dp[i][j] %= MOD
    #     # print(dp)
    #     def dfs(cur):
    #         if cur == -1:
    #             return 0, 1
    #         left_cnt, left_res = dfs(node[cur][0])
    #         right_cnt, right_res = dfs(node[cur][-1])
    #         res = left_res*right_res*dp[left_cnt+right_cnt][left_cnt]
    #         res %= MOD
    #         return left_cnt+right_cnt+1 ,res 
    #     return dfs(nums[0])[-1]-1

    def numOfWays(self, nums: List[int]) -> int:
        def f(nums):
            if len(nums) <= 2: return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            return comb(len(left)+len(right), len(right)) * f(left) * f(right) % (10**9+7)
        return (f(nums)-1) % (10**9+7)