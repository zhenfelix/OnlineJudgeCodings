class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        sums, res = 0, []
        for x in nums:
            sums ^= x 
        total = (1<<maximumBit)-1
        for x in nums[::-1]:
            res.append(sums^total)
            sums ^= x 
        return res 