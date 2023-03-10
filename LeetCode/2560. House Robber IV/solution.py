class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        lo, hi = 0, max(nums)
        nums.append(inf)
        def check(t):
            cnt, cur = 0, 0
            for x in nums:
                if x <= t:
                    cur += 1
                else:
                    cnt += (cur+1)//2
                    cur = 0
            return cnt 
            
        while lo <= hi:
            m = (lo+hi)//2
            if check(m) >= k:
                hi = m-1
            else:
                lo = m+1
        return lo