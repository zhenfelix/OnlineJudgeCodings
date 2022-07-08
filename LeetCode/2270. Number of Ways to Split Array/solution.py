class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        tot = sum(nums)
        cnt = 0
        sums = 0
        for i in range(n-1):
            sums += nums[i]
            if sums >= tot-sums:
                cnt += 1
        return cnt