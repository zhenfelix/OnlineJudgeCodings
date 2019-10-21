class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = max(nums), sum(nums)
        # print(lo,hi)
        
        while lo <= hi:
            cur = cnt = 0
            mid = (lo+hi)//2
            for num in nums:
                cur += num
                if cur > mid:
                    cnt += 1
                    cur = num 
                    if cnt + 1 > m:
                        break
            if cnt + 1 > m:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

