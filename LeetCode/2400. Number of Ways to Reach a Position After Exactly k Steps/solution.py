class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9+7
        if endPos < startPos:
            endPos, startPos = startPos, endPos
        d = endPos-startPos
        if (d+k)%2 or d > k:
            return 0
        x = (d+k)//2
        return math.comb(k,x)%MOD