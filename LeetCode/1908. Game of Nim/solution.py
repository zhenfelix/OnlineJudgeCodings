class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        ans = 0
        for x in piles:
            ans ^= x
        return ans != 0

class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        n = len(piles)
        @cache
        def dfs(arr):
            arr = list(arr)
            if all(a == 0 for a in arr):
                return False
            for i in range(n):
                for j in range(arr[i]):
                    if not dfs(tuple(arr[:i]+[j]+arr[i+1:])):
                        return True
            return False
        return dfs(tuple(piles))