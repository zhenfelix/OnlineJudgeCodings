# class Solution:
#     def maxSizeSlices(self, slices: List[int]) -> int:
#         n = len(slices) // 3
#         def linear(arr):
#             eat = [[0] + [-math.inf]*n] * 2
#             for x in arr:
#                 eat.append([i and max(eat[-1][i], eat[-2][i-1]+x) for i in range(n+1)])
#             return max(l[n] for l in eat)
#         return max(linear(slices[1:]), linear(slices[:-1]))

# class Solution:
#     def maxSizeSlices(self, slices: List[int]) -> int:
#         n = len(slices) // 3
#         def linear(arr):
#             eat = collections.deque([[0] + [-math.inf]*n] * 2)
#             res = 0
#             for x in arr:
#                 eat += [i and max(eat[-1][i], eat[-2][i-1]+x) for i in range(n+1)],
#                 eat.popleft()
#                 res = max(res, eat[-1][n])
#             return res
#         return max(linear(slices[1:]), linear(slices[:-1]))
    
# Excellent explanation with math proof on Quora
# https://leetcode.com/problems/pizza-with-3n-slices/discuss/546574/Excellent-explanation-with-math-proof-on-Quora

import functools
class Solution:
    # def maxSizeSlices(self, slices: List[int]) -> int:
    #     n = len(slices) // 3
    #     @functools.lru_cache(None)
    #     def dfs(i,cnt):
    #         if i < 0:
    #             return 0 if cnt == 0 else -float('inf')
    #         if cnt == 0:
    #             return 0
    #         if i < (cnt-1)*2:
    #             return -float('inf')
    #         return max(arr[i]+dfs(i-2,cnt-1), dfs(i-1,cnt))
    #     res = 0
    #     arr = slices[1:]
    #     res = max(res, dfs(len(arr)-1,n))
    #     dfs.cache_clear()
    #     arr = slices[:-1]
    #     res = max(res, dfs(len(arr)-1,n))
    #     return res
    
    def maxSizeSlices(self, A):
        @functools.lru_cache(None)
        def dp(i, j, k, cycle=0):
            if k == 1: return max(A[i:j + 1])
            if j - i + 1 < k * 2 - 1: return -float('inf')
            return max(dp(i + cycle, j - 2, k - 1) + A[j], dp(i, j - 1, k))
        return dp(0, len(A) - 1, len(A) // 3, 1)