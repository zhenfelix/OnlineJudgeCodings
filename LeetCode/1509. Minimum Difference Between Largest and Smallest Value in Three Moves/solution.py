class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        return min(nums[-i]-nums[4-i] for i in range(1,5))