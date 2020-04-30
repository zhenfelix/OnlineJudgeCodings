class Solution:
#     def maxValueAfterReverse(self, nums: List[int]) -> int:
#         maxi, mini = -math.inf, math.inf
        
#         for a, b in zip(nums, nums[1:]):
#             maxi = max(min(a, b), maxi)
#             mini = min(max(a, b), mini)
#         change = max(0, (maxi - mini) * 2)
        
#         # solving the boundary situation
#         for a, b in zip(nums, nums[1:]):
#             tmp1 = - abs(a - b) + abs(nums[0] - b)
#             tmp2 = - abs(a - b) + abs(nums[-1] - a)
#             change = max([tmp1, tmp2, change])
            
#         original_value = sum(abs(a - b) for a, b in zip(nums, nums[1:]))
#         return  original_value + change

    def maxValueAfterReverse(self, A):
        total, res, min2, max2 = 0, 0, float('inf'), -float('inf')
        for a, b in zip(A, A[1:]):
            total += abs(a - b)
            res = max(res, abs(A[0] - b) - abs(a - b))
            res = max(res, abs(A[-1] - a) - abs(a - b))
            min2, max2 = min(min2, max(a, b)), max(max2, min(a, b))
        return total + max(res, (max2 - min2) * 2)