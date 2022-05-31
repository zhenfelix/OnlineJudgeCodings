class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo, hi = 1, max(candies)
        while lo <= hi:
            mid = (lo+hi)//2
            cnt = sum(c//mid for c in candies)
            if cnt >= k:
                lo = mid+1
            else:
                hi = mid-1
        return hi