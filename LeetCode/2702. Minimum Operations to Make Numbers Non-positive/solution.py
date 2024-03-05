class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        lo, hi = 1, sum(nums)
        while lo <= hi:
            def check(cnt):
                cur = 0
                for a in nums:
                    if a-cnt*y > 0 and x-y < 0:
                        return False
                    if a-cnt*y <= 0: continue
                    cur += max(0,(a-cnt*y-1)//(x-y)+1)
                return cur <= cnt  
            if check((lo+hi)//2):
                hi = (lo+hi)//2-1
            else:
                lo = (lo+hi)//2+1
        return lo 


