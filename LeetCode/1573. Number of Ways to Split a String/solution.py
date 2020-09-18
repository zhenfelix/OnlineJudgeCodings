class Solution:
    def numWays(self, s: str) -> int:
        cc = Counter()
        cur, n = 0, len(s)
        MOD = 10**9+7
        for ch in s:
            if ch == '1':
                cur += 1
            cc[cur] += 1
        if cur%3 != 0:
            return 0
        if cur == 0:
            return ((n-2)*(n-1)//2)%MOD
        return cc[cur//3]*cc[cur//3*2]%MOD