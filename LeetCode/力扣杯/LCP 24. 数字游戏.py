from heapq import *

class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        MOD = 10**9+7
        large, small = [nums[0]], []
        level = large[0]
        n, sums = len(nums), 0
        res = [0]
        for i in range(1,n):
            cur = nums[i] - i 
            sums += abs(level-cur)
            heappush(small, -heappushpop(large, cur))
            if len(large) < len(small):
                heappush(large, -heappop(small))
                sums -= abs(large[0] - level)
            sums%=MOD
            level = large[0]
            res.append(sums)
        return res

