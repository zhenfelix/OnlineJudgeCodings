class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        tot = sum(nums)
        n = len(nums)
        ans = float('inf')
        idx = -1
        s = 0
        for i in range(n):
            s += nums[i]
            left = s//(i+1)
            right = 0 if i == n-1 else (tot-s)//(n-i-1)
            if abs(left-right) < ans:
                ans = abs(left-right)
                idx = i
        return idx