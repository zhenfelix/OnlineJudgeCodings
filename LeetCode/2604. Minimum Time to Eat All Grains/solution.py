class Solution:
    def minimumTime(self, hens: List[int], grains: List[int]) -> int:
        hens.sort()
        grains.sort()
        # print(hens)
        # print(grains)
        lo, hi = 0, 2*10**9
        while lo <= hi:
            t = (lo+hi)//2
            n = len(grains)
            j = 0
            for g in hens:
                pj = j
                while j < n and min(abs(grains[pj]-g),abs(grains[j]-g))+grains[j]-grains[pj] <= t:
                    j += 1
                # print(g,j)
            # print(t,j)
            if j >= n:
                hi = t-1
            else:
                lo = t+1
        return lo 
