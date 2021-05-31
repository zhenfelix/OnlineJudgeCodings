class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n//2):
            res = max(res, nums[i]+nums[n-1-i])
        return res



    def minPairSum(self, A):
        return max(a + b for a, b in zip(sorted(A), sorted(A)[::-1]))