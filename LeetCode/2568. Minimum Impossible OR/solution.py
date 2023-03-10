class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(32):
            if (1<<i) not in nums:
                return 1<<i 
        return -1

