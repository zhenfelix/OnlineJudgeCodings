class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mp = Counter()
        res = 0
        for x in nums:
            res += mp[x-k]
            res += mp[x+k]
            mp[x] += 1
        return res