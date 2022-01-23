class Solution:
    def countElements(self, nums: List[int]) -> int:
        lo, hi = min(nums), max(nums)
        return sum(lo < x < hi for x in nums)