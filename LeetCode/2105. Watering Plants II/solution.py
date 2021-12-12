class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        lo, hi = 0, n-1
        cnt = 0
        ca, cb = capacityA, capacityB
        while lo <= hi:
            if lo == hi:
                if ca >= cb:
                    if ca < plants[lo]:
                        cnt += 1
                    lo += 1
                else:
                    if cb  < plants[hi]:
                        cnt += 1
                    hi -= 1
            else:
                if ca < plants[lo]:
                    ca = capacityA
                    cnt += 1
                ca -= plants[lo]
                lo += 1
                if cb < plants[hi]:
                    cb = capacityB
                    cnt += 1
                cb -= plants[hi]
                hi -= 1
        return cnt 

