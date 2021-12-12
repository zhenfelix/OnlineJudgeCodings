class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        rs, cs = startPos
        rh, ch = homePos
        tot = 0
        delta = 1 if rh >= rs else -1
        for r in range(rs,rh,delta):
            tot += rowCosts[r+delta]
        delta = 1 if ch >= cs else -1
        for c in range(cs,ch,delta):
            tot += colCosts[c+delta]
        return tot