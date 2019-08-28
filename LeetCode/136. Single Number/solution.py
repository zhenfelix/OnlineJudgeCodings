class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for a in nums:
            x ^= a
        return x