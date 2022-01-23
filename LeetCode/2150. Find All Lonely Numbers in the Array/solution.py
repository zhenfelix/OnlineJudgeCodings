class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cc = Counter(nums)
        res = []
        for x in nums:
            if cc[x] == 1 and cc[x-1] == 0 and cc[x+1] == 0:
                res.append(x)
        return res