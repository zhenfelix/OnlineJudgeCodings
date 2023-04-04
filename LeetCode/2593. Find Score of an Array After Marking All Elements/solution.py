class Solution:
    def findScore(self, nums: List[int]) -> int:
        hq = [(v,i) for i, v in enumerate(nums)]
        heapify(hq)
        n = len(nums)
        s = 0
        while hq:
            v, i = heappop(hq)
            if nums[i] == -1: continue
            s += v  
            nums[i] = -1
            if i: nums[i-1] = -1
            if i+1 < n: nums[i+1] = -1
        return s 