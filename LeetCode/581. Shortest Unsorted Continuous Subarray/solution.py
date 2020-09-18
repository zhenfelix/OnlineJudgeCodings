# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         sorted_nums = sorted(nums)
#         left, right = 0, len(nums)-1
#         while left <= right and nums[left] == sorted_nums[left]:
#             left += 1
#         while left <= right and nums[right] == sorted_nums[right]:
#             right -= 1
#         return right-left+1


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        mi, mx, n = float('inf'), -float('inf'), len(nums)
        for i in range(n-1):
            if nums[i+1] < nums[i]:
                mx = max(mx, nums[i])
                mi = min(mi, nums[i+1])
        left, right = 0, n-1
        while left <= right and nums[left] <= mi:
            left += 1
        while left <= right and nums[right] >= mx:
            right -= 1
        # print(mi,mx)
        # print(left, right)
        return max(0,right-left+1)