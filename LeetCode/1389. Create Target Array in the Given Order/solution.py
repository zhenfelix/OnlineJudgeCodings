class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i, n in zip(index,nums):
            res.insert(i,n)
        return res