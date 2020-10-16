class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        sums = 0
        for a in nums:
            sums ^= a
        return sums == 0 or len(nums) & 1 == 0
        

from functools import reduce

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return reduce(lambda x, y: x^y, nums) == 0 or len(nums) & 1 == 0
        