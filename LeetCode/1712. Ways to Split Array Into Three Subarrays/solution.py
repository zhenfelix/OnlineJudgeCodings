class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        total = sum(nums)
        cnt, MOD, cur = 0, 10**9+7, 0
        arr = []
        for i in range(len(nums)-1):
            cur += nums[i]
            hi = bisect.bisect_right(arr,cur//2)
            lo = bisect.bisect_left(arr,cur*2-total)
            if hi > lo:
                cnt += (hi-lo)
                cnt %= MOD
            arr.append(cur)
        return cnt 


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        total = sum(nums)
        cnt, MOD, cur = 0, 10**9+7, 0
        arr = []
        lo, hi = 0, 0
        for i in range(len(nums)-1):
            cur += nums[i]
            while hi < len(arr) and arr[hi] <= cur//2:
                hi += 1
            while lo < len(arr) and arr[lo] < 2*cur-total:
                lo += 1
            if hi > lo:
                cnt += (hi-lo)
                cnt %= MOD
            arr.append(cur)
        return cnt 