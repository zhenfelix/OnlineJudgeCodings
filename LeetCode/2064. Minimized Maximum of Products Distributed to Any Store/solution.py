class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo, hi = 1, 10**5
        def check(x):
            cnt = 0
            for y in quantities:
                cnt += (y+x-1)//x 
                if cnt > n:
                    return False
            return True

        while lo <= hi:
            mid = (lo+hi)//2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
