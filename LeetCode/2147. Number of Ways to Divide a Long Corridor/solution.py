class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9+7
        cnt = 0 
        last = -1
        res = 1
        for i, ch in enumerate(corridor):
            if ch == 'S':
                if cnt%2 == 0 and last != -1:
                    res *= (i-last)
                    res %= MOD
                cnt += 1 
                last = i 
        if cnt%2 != 0 or cnt == 0:
            return 0 
        return res