class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        right = sums = sum(nums)
        for i in range(n):
            right -= nums[i]
            if sums-nums[i] == 2*right:
                return i 
        return -1
