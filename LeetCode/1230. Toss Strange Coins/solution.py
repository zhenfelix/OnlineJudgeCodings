
# from functools import reduce
class Solution:
    # def probabilityOfHeads(self, prob: List[float], target: int) -> float:
    #     def dfs(n,t):
    #         if (n,t) in memo:
    #             return memo[n,t]
    #         if t > n:
    #             memo[n,t] = 0
    #             return 0
    #         if n == 1:
    #             p = [1-prob[0],prob[0]]
    #             memo[n,t] = p[t]
    #             return memo[n,t]
    #         if t == 0:
    #             memo[n,t] = reduce(lambda a,b: a*b, [1-x for x in prob[:n]])
    #             return memo[n,t]
    #         memo[n,t] = dfs(n-1,t)*(1-prob[n-1]) + dfs(n-1,t-1)*prob[n-1]
    #         return memo[n,t]
    #     memo = {}
    #     return dfs(len(prob),target)
    
    
    def probabilityOfHeads(self, prob, target):
        dp = [1] + [0] * target
        for p in prob:
            for k in range(target, -1, -1):
                dp[k] = (dp[k - 1] if k else 0) * p + dp[k] * (1 - p)
        return dp[target]


