class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        cost += [0]
        res, pre, sums, cur = 0, '?', 0, 0
        for i, ch in enumerate(s+'?'):
            if ch != pre:
                res += sums-cur
                sums = 0
                cur = 0
            sums += cost[i]
            cur = max(cur, cost[i])
            pre = ch 
        return res


    def minCost(self, s, cost):
        res = max_cost = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            res += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])
        return res