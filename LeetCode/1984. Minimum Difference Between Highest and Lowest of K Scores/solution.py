class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        mx = 10**5
        n = len(nums)
        nums.sort()
        for i in range(n-k+1):
            mx = min(mx, nums[i+k-1]-nums[i])
        return mx