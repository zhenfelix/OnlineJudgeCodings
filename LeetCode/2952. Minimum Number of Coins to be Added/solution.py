class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        reach = 0
        ans = 0
        for i, a in enumerate(coins):
            if reach >= target: break
            while a > reach+1:
                ans += 1
                reach += reach+1
            reach += a 
        while reach < target:
            ans += 1
            reach += reach+1
        return ans 