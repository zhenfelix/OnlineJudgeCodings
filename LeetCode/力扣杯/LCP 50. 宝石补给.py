class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            delta = gem[x]//2
            gem[x] -= delta
            gem[y] += delta
        return max(gem)-min(gem)
