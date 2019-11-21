class Solution:
    def maxSumDivThree(self, A):
        seen = [0, -10**9 - 1, -10**9]
        for a in A:
            for i in [a + x for x in seen]:
                seen[i % 3] = max(seen[i % 3], i)
        return seen[0]

# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         sums = sum(nums)
#         q1, q2 = [], []

#         for num in nums:
#             if num%3 == 1:
#                 q1.append(num)
#             elif num%3 == 2:
#                 q2.append(num)

#         q1.sort()
#         q2.sort()
#         len1, len2 = len(q1), len(q2)

#         res = []
#         for i in range(min(len1+1,3)):
#             for j in range(min(len2+1,3)):
#                 tmp = sums - sum(q1[:i]) - sum(q2[:j])
#                 # print(i,j,tmp)
#                 if tmp%3 == 0:
#                     res.append(tmp)
#         if not res:
#             return 0
#         return max(res)


# from functools import lru_cache
# class Solution:
#     def maxSumDivThree(self, A):
#         @lru_cache(None)
#         def dfs(idx, mod):
#             if idx == n:
#                 return 0 if mod == 0 else -float('inf')
#             return max(dfs(idx+1, mod), dfs(idx+1, (mod+A[idx])%3))
#         return dfs(0, 0)
