class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        nums.sort()
        f = [1]*(n+1)
        for i in range(1,n+1):
            f[i] = (f[i-1]*2)%MOD
        right = n-1
        ans = 0
        for left in range(n):
            while left <= right and nums[left]+nums[right] > target:
                right -= 1
            if left > right:
                break
            ans = (ans+f[right-left])%MOD
        return ans 

            


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        if nums[0] * 2 > target:
            return 0
        left = 0
        right = len(nums) - 1
        res = 0
        mode = 1_0000_0000_7
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += (1 << (right-left))
                res %= mode
                left += 1
            else:
                right -= 1
        return res
