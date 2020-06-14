class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for x, y in zip(nums[:n],nums[n:]):
            res += [x,y]
        return res
        