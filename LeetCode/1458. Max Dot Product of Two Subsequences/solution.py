from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,j,empty):
            if i == -1 or j == -1:
                return 0 if empty else -float('inf')
            # if i == 0:
            #     return max(nums1[0]*nums2[k] for k in range(j+1))
            # if j == 0:
            #     return max(nums2[0]*nums1[k] for k in range(i+1))
            return max(dfs(i-1,j,empty),dfs(i,j-1,empty),dfs(i-1,j-1,True)+nums1[i]*nums2[j])
        n, m = len(nums1), len(nums2)
        return dfs(n-1,m-1,False)


# from functools import lru_cache
# class Solution:
#     def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
#         @lru_cache(None)
#         def helper(i, j):
#             if i == 0 or j == 0: return -math.inf
#             return max(helper(i, j - 1), helper(i - 1, j),
#                        max(helper(i - 1, j - 1), 0) + nums1[i - 1] * nums2[j - 1])
#         return helper(len(nums1), len(nums2))

# class Solution:
#     def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
#         n, m = len(nums1), len(nums2)
#         dp = [-math.inf] * (m + 1)
#         for i in range(1, n + 1):
#             dp, old_dp = [-math.inf], dp
#             for j in range(1, m + 1):
#                 dp += max(
#                     old_dp[j], # not select i
#                     dp[-1], # not select j
#                     # old_dp[j - 1], # not select either
#                     max(old_dp[j - 1], 0) + nums1[i - 1] * nums2[j - 1], # select both
#                 ),
#         return dp[-1]    

class Solution:
    def maxDotProduct(self, A, B):
        n, m = len(A), len(B)
        dp = [[0] * (m) for i in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = A[i] * B[j]
                if i and j: dp[i][j] += max(dp[i - 1][j - 1], 0)
                if i: dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j: dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]