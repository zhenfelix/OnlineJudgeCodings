class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        A, B = [nums[i] for i in range(n) if i&1 == 0], [nums[i] for i in range(n) if i&1 == 1]
        res = []
        for a, b in zip(A,B):
            res += [b]*a
        return res
        