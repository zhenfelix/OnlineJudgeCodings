class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo <= hi:
            mid = (lo+hi)//2
            cur = day = 0
            for w in weights:
                cur += w
                if cur > mid:
                    day += 1
                    cur = w
                if day + 1 > D:
                    break
            if day + 1 > D:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo