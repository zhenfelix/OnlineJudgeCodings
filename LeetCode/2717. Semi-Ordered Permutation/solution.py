class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        a, b = nums.index(1), nums.index(len(nums))
        if a < b:
            return a + len(nums) - b - 1
        else:
            return a + len(nums) - b - 2

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = -1, -1
        for i, v in enumerate(nums):
            if v == 1: a = i 
            if v == n: b = i
        delta = 0
        if a > b:
            delta = 1
        return a+n-1-b-delta