class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        ans, cnt = 0, 0
        for a in nums:
            if a == mx:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0 
        return ans