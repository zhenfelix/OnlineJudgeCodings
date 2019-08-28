class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tag = 0
        for x in nums:
            tag ^= x
        tag = tag & (tag ^ (tag-1))
        a, b = 0, 0
        for x in nums:
            if tag & x != 0:
                a ^= x
            else:
                b ^= x
        return [a,b]
        