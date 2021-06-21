class Solution:
    def leastMinutes(self, n: int) -> int:
        cnt, cur = 0, 1
        while cur < n:
            cur *= 2
            cnt += 1
        return cnt+1
        