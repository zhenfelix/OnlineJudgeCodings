class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = set([0])
        ans = curr = 0
        
        for i, num in enumerate(nums):
            curr += num
            prev = curr - target
            if prev in seen:
                ans += 1
                seen = set()
            seen.add(curr)
        
        return ans


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pre, sums, cnt = -1, 0, 0
        mp = {0: -1}
        for i, x in enumerate(nums):
            sums += x
            if sums-target in mp and mp[sums-target] >= pre:
                cnt += 1
                pre = i 
            mp[sums] = i 
        return cnt


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        mp = {0: 0}
        cursum = 0
        for i, v in enumerate(nums):
            dp[i+1] = dp[i]
            cursum += v 
            if cursum-target in mp:
                dp[i+1] = max(dp[i+1], dp[mp[cursum-target]]+1)
            mp[cursum] = i+1
        return max(dp)