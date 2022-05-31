class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cc = Counter(nums)
        return all(v%2 == 0 for k, v in cc.items())