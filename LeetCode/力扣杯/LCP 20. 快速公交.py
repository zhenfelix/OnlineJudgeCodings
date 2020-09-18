from functools import lru_cache
class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        @lru_cache(None)
        def min_cost(target):
            
            if target == 0:
                return 0
            cur_cost = inc * target
            for i in range(len(jump)):
                if target % jump[i] == 0:
                    cur_cost = min(cur_cost, min_cost(target // jump[i]) + cost[i])
                    continue
                cur_cost = min(cur_cost, min_cost(target // jump[i]) + cost[i] + (target % jump[i]) * inc)
                if target > 1:
                    cur_cost = min(cur_cost, min_cost(target // jump[i] + 1) + cost[i] + (jump[i] - target % jump[i]) * dec)
            return cur_cost
        p = 10 ** 9 + 7
        return min_cost(target) % p
        
