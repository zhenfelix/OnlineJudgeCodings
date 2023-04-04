class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        hpq = [(v, v, 1)for v in ranks]
        heapify(hpq)
        for _ in range(cars):
            ans, v, c = heappop(hpq)
            c += 1
            heappush(hpq, (v * c * c, v, c))
        return ans


# 作者：小羊肖恩
# 链接：https://leetcode.cn/circle/discuss/Gx4OWK/view/mXp5Ho/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def calc(r, t):
            # lo, hi = 0, t 
            # while lo <= hi:
            #     mid = (lo+hi)//2
            #     if r*mid*mid <= t:
            #         lo = mid + 1
            #     else:
            #         hi = mid - 1
            return int(sqrt(t//r))

        l, r = 1, cars*cars*min(ranks)
        while l <= r:
            m = (l+r)//2
            cnt = sum(calc(r,m) for r in ranks)
            if cnt >= cars:
                r = m-1
            else:
                l = m+1
        return l 