class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cnt, j = 0, 0
        for a in nums:
            while j < n and a >= nums[j]:
                j += 1
            if j < n:
                cnt += 1
                j += 1
        return cnt