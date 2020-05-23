# import functools
# class Solution:
#     def largestNumber(self, cost: List[int], target: int) -> str:
#         @functools.lru_cache(None)
#         def dfs(remains):
#             if remains < 0:
#                 return '0'
#             if remains == 0:
#                 return ''
#             res = '0'
#             for i in range(9):
#                 cur = dfs(remains-cost[i])
#                 if cur == '0':
#                     continue
#                 cur = str(i+1)+cur
#                 if len(cur) > len(res) or (len(cur) == len(res) and cur > res):
#                     res = cur
#             return res
#         return dfs(target)

class Solution:
    def largestNumber(self, cost, target):
        dp = [0] + [-1] * (target + 5000)
        for t in range(1, target + 1):
            dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
        return str(max(dp[t], 0))    