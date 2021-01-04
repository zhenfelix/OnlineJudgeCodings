class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        mp = {}
        for i, x in enumerate(target):
            mp[x] = i 
        nums = []
        for x in arr:
            if x not in mp:
                continue
            cur = mp[x]
            idx = bisect.bisect_left(nums,cur)
            if idx == len(nums):
                nums.append(float('inf'))
            nums[idx] = cur
        return len(target)-len(nums)