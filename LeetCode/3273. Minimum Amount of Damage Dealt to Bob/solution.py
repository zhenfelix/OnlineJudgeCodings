class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        costs = [(h-1)//power+1 for h in health]
        # print(costs)
        arr = [(c/d,c,d) for d,c in zip(damage,costs)]
        arr.sort()
        # print(arr)
        ans = 0
        t = 0
        for _, c, d in arr:
            t += c
            ans += t*d  
        return ans 