import bisect

# class Solution:
#     def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
#         n = len(matrix)
#         if n == 0:
#             return 0
#         m = len(matrix[0])
#         ans = -float('inf')
#         for left in range(m):
#             nums = [0]*n
#             for right in range(left,m):
#                 for i in range(n):
#                     nums[i] += matrix[i][right]
#                 # tmp = -float('inf')
#                 arr = [0]
#                 curSum = 0
#                 for cur in nums:
#                     curSum += cur
#                     idx = bisect.bisect_left(arr,curSum-k)
#                     if idx < len(arr):
#                         ans = max(ans, curSum-arr[idx])
#                     bisect.insort(arr,curSum)
#         return ans

class Solution:
    def maxSumSubmatrix(self, matrix, k):
            """
            :type matrix: List[List[int]]
            :type k: int
            :rtype: int
            """
            if not matrix:  return 0
            
            res = float('-inf')
            rows, columns = len(matrix), len(matrix[0])
            for i in range(columns):
                sums = [0 for _ in range(rows)]
                for j in range(i, columns):
                    for r in range(rows):
                        sums[r] += matrix[r][j]
                    # find the largest sum of a subarray which is no more than K
                    # import bisect
                    cum_sum = [0]
                    cum, max_sum = 0, float('-inf')
                    for item in sums:
                        cum += item
                        left = bisect.bisect_left(cum_sum, cum - k)
                        if left < len(cum_sum):
                            max_sum = max(max_sum, cum - cum_sum[left])
                        bisect.insort(cum_sum, cum)
                    res = max(res, max_sum)
            return res