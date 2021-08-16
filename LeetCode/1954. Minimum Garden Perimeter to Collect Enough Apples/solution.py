class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        lo, hi = 1, 10**6
        while lo <= hi:
            mid = (lo+hi)//2
            cnt = 2*mid*(mid+1)*(2*mid+1)
            if cnt >= neededApples:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo*8