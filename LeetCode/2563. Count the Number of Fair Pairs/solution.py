class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        l, r = n-1, n-1 
        for i in range(n):
            while l >= 0 and nums[i]+nums[l] >= lower:
                l -= 1
            while r >= 0 and nums[i]+nums[r] > upper:
                r -= 1
            if l < r:
                ans += r-l
                if l < i <= r:
                    ans -= 1
        return ans//2