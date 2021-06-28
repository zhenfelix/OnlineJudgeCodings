class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        odd, even = nums[0], 0
        for i in range(1,n):
            x = nums[i]
            odd, even = max(odd, even+x), max(even, odd-x)
        return max(odd, even)