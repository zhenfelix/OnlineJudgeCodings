class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        tot, cnt = 0, 0
        cc = Counter()
        for i, x in enumerate(nums):
            tot += i 
            cnt += cc[x-i]
            cc[x-i] += 1
        return tot-cnt