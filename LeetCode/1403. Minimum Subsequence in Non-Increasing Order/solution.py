class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x:-x)
        total, sums = sum(nums), 0
        cur = 0
        while sums*2 <= total:
            sums += nums[cur]
            cur += 1
        return nums[:cur]