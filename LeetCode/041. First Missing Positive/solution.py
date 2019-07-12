# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         n = len(nums)
#         for idx in range(n):
#             if nums[idx] > 0 and idx+1 != nums[idx]:
#                 move = nums[idx] - 1
#                 while move >= 0 and move < n and move+1 != nums[move]:
#                     tmp = nums[move]
#                     nums[move] = move+1
#                     move = tmp - 1
#         for idx, num in enumerate(nums):
#             if idx+1 != num:
#                 return idx+1
#         return n+1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for idx in range(n):
            move = nums[idx] - 1
            while move >= 0 and move < n and move+1 != nums[move]:
                nums[move], nums[idx] = nums[idx], nums[move]
                move = nums[idx] - 1

        for idx, num in enumerate(nums):
            if idx+1 != num:
                return idx+1
        return n+1