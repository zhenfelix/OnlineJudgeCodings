# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         i = n-2
#         while i >= 0 and nums[i] >= nums[i+1]:
#             i -= 1
#         if i >= 0:
#             j = n-1
#             while nums[i] >= nums[j]:
#                 j -= 1
#             nums[i], nums[j] = nums[j], nums[i]
#         i, j = i+1, n-1
#         while i < j:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#             j -= 1
#         return

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = n - 1
        while left-1 >= 0 and nums[left] <= nums[left-1]:
            left -= 1
        if left > 0:
            idx = n - 1
            while nums[idx] <= nums[left-1]:
                idx -= 1
            nums[left-1], nums[idx] = nums[idx], nums[left-1]
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return