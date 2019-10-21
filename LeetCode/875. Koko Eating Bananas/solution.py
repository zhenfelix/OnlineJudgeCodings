class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo, hi = max(1,sum(piles)//H), max(piles)
        # print(lo,hi)
        while lo <= hi:
            mid = (lo+hi)//2
            cnt = 0
            for pile in piles:
                cnt += pile//mid + (pile%mid != 0)
                if cnt > H:
                    break
            if cnt > H:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo