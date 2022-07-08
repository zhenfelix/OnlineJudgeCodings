class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort(reverse = True)
        arr = [(v,i) for i, v in enumerate(spells)]
        arr.sort(reverse = True)
        ans = [-1]*len(spells)
        for v, i in arr:
            while potions and potions[-1]*v < success:
                potions.pop()
            ans[i] = len(potions)
        return ans