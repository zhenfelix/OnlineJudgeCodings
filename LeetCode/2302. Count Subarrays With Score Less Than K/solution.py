class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        sums = 0
        n = len(nums)
        for right in range(n):
            sums += nums[right]
            while left <= right and sums*(right-left+1) >= k:
                sums -= nums[left]
                left += 1
            ans += right-left+1
        return ans