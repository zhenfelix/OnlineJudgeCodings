class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()
        diff = [inf]*n 
        for i in range(n-1):
            diff[i] = nums[i+1]-nums[i]
        lo, hi = 0, max(nums)
        while lo <= hi:
            mid = (lo+hi)//2
            def check(x):
                cnt = 0
                pre = False
                for i in range(n-1):
                    if diff[i] <= x and not pre:
                        cnt += 1
                        pre = True
                    else:
                        pre = False
                    if cnt >= p:
                        return True
                return False
            if check(mid):
                hi = mid-1
            else:
                lo = mid+1
        return lo





class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()
        diff = [inf]*n 
        for i in range(n-1):
            diff[i] = nums[i+1]-nums[i]
        lo, hi = 0, max(nums)
        while lo <= hi:
            mid = (lo+hi)//2
            def check(x):
                dp = [0]*n 
                for i in range(n-1):
                    if diff[i] <= x:
                        dp[i] = max(dp[i],dp[i-2]+1)
                    dp[i] = max(dp[i],dp[i-1])
                    if dp[i] >= p:
                        return True
                return False
            if check(mid):
                hi = mid-1
            else:
                lo = mid+1
        return lo



