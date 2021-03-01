# class Solution:
#     def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
#         toppingCosts = sorted(toppingCosts*2)
        
#         @cache
#         def fn(i, x):
#             """Return sum of subsequence of toppingCosts[i:] closest to x."""
#             if i == len(toppingCosts): return 0
#             return min(fn(i+1, x), toppingCosts[i] + fn(i+1, x-toppingCosts[i]), key=lambda y: (abs(y-x), y))
        
#         ans = inf
#         for bc in baseCosts: 
#             ans = min(ans, bc + fn(0, target - bc), key=lambda x: (abs(x-target), x))
#         return ans 

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = [float('inf')]
        n = len(toppingCosts)
        def dfs(idx,cnt,sums):
            if idx == n:
                return
            if cnt == 3:
                return
            if sums - target >= abs(res[-1] - target):
                return
            if abs(sums-target) <= abs(res[-1] - target):
                res[-1] = sums 
            dfs(idx,cnt+1,sums+toppingCosts[idx])
            dfs(idx+1,0,sums)
        for base in baseCosts:
            dfs(0,0,base)
        return res[-1]
