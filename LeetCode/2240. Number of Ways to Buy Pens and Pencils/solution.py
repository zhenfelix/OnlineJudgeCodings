class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        cur = 0
        while cur <= total:
            ans += (total-cur)//cost2+1
            cur += cost1
        return ans
