class Solution:
    def maxInvestment(self, product: List[int], limit: int) -> int:
        lo, hi = 1, max(product)
        while lo <= hi:
            mid = (lo+hi)//2
            cnt = sum(p-mid+1 for p in product if p >= mid)
            if cnt <= limit:
                hi = mid-1
            else:
                lo = mid+1
        cnt = sum(p-lo+1 for p in product if p >= lo)
        # print(lo,cnt)
        return ((lo-1)*(limit-cnt)+sum((lo+p)*(p-lo+1)//2 for p in product if p >= lo))%(10**9+7)