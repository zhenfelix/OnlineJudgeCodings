class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        # print(price)
        def check(t):
            n = len(price)
            cnt = [1]*n 
            j = 0
            mx = 0
            for i in range(1,n):
                while j < i and price[i]-price[j] >= t:
                    mx = max(mx, cnt[j])
                    j += 1
                cnt[i] = mx+1
            # print(t,cnt)
            return max(cnt)
        lo, hi = 0, price[-1]-price[0]
        while lo <= hi:
            m = (lo+hi)//2
            if check(m) >= k:
                lo = m + 1
            else:
                hi = m - 1
        return hi 
