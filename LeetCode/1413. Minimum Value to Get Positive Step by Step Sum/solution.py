class Solution(object):
    def minStartValue(self, nums):
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        return max(1, 1 - min(prefix))
        
        # bonus one-liner
        return max(1, 1 - min(itertools.accumulate(nums)))


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start, res = 0, float('inf')
        for num in nums:
            start += num
            res = min(res,start)
        return max(1,1-res)
        