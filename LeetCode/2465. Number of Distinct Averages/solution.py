class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)
        nums.sort()
        i, j = 0, n-1
        while i < j:
            seen.add(nums[i]+nums[j])
            i += 1
            j -= 1
        return len(seen)