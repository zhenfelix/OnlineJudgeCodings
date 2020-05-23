class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        while left < right:
            while left < right and nums[left] & 1 == 1:
                left += 1
            while left < right and nums[right] & 1 == 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums