class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        lo, hi = 1, n 
        while lo <= hi:
            m = (lo+hi)//2
            if m*(m+1)//2 <= n:
                lo = m + 1
            else:
                hi = m - 1
        return hi

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        cnt, cur = 1, 1
        while cur < n-cur:
            cnt += 1
            n -= cur
            cur += 1
        return cnt