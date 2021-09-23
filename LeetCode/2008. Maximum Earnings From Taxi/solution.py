from functools import lru_cache

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key = lambda x : x[1])
        finish = [e for s,e,c in rides]
        # print(rides)
        # print(finish)

        @lru_cache(None)
        def dfs(i):
            if i < 0:
                return 0;  
            s, e, c = rides[i]
            idx = bisect.bisect_right(finish,s)-1
            print(i,idx)
            return max(dfs(i-1),dfs(idx)+e-s+c)
        return dfs(len(rides)-1)
