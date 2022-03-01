class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        mi, mx = min(time), max(time)
        lo, hi = 0, totalTrips*mi
        while lo <= hi:
            mid = (lo+hi)//2
            tot = sum(mid//t for t in time)
            if tot >= totalTrips:
                hi = mid-1
            else:
                lo = mid+1
        return lo