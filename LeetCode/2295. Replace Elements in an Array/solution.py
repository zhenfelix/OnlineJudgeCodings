class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {v: i for i, v in enumerate(nums)}
        for a, b in operations:
            i = mp[a]
            nums[i] = b
            mp[b] = i
        return nums