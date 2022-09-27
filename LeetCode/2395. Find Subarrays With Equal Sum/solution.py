class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for i in range(n-1):
            s = sum(nums[i:i+2])
            if s in seen:
                return True
            seen.add(s)
        return False