# from functools import lru_cache
# class Solution:
#     def stoneGameVII(self, stones: List[int]) -> int:
#         presum = [0]
#         for x in stones:
#             presum.append(presum[-1]+x)
#         @lru_cache(None)
#         def dfs(left,right):
#             if left == right:
#                 return 0
#             res = max(presum[right+1]-presum[left+1]-dfs(left+1,right),presum[right]-presum[left]-dfs(left,right-1))
#             # print(left,right,res)
#             return res
#         ans = dfs(0,len(stones)-1)
#         dfs.cache_clear()
#         return ans


from functools import lru_cache
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        presum = [0]
        n = len(stones)
        for x in stones:
            presum.append(presum[-1]+x)
        dp = [[0]*n for _ in range(n)]
        for delta in range(1,n):
            for right in range(delta,n):
                left = right - delta
                dp[left][right] = max(presum[right+1]-presum[left+1]-dp[left+1][right],presum[right]-presum[left]-dp[left][right-1])

        return dp[0][-1]