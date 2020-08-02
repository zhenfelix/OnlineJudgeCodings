class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cc = Counter()
        res = 0
        for x in nums:
            res += cc[x]
            cc[x] += 1
        return res