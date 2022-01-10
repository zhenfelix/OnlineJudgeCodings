class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)
        res = k
        cur = 0
        for i in range(n+k):
            cur += nums[i%n]
            if i-k >= 0:
                cur -= nums[i-k]
            res = min(res, k-cur)
        return res