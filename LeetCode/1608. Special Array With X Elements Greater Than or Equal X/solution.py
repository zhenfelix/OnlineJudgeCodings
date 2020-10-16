# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         nums.sort(reverse=True)
#         i = 0
#         while i < len(nums) and nums[i] >= i:
#             i += 1
#         if nums[i - 1] < i: return -1
#         return i

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and i == nums[i] else i

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1 if left < len(nums) and left == nums[left] else left



class Solution:
    def specialArray(self, nums: List[int]) -> int:
        mi, mx = 0, 1000
        for x in range(mi,mx+1):
            if sum(a >= x for a in nums) == x:
                return x
        return -1