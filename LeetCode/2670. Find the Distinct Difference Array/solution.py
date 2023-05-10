class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0]*(n+1)
        right = [0]*(n+1)
        seen = set()
        for i in range(n):
            seen.add(nums[i])
            left[i] = len(seen)
        seen = set()
        for i in range(n)[::-1]:
            seen.add(nums[i])
            right[i] = len(seen)
        diff = [0]*n 
        for i in range(n):
            diff[i] = left[i]-right[i+1]
        return diff