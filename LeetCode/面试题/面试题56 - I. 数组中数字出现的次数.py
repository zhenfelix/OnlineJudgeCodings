class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = []
        t, a, b = 0, 0, 0
        for num in nums:
            t ^= num
        t = t & (-t)
        for num in nums:
            if num & t:
                a ^= num 
            else:
                b ^= num 
        return [a,b]