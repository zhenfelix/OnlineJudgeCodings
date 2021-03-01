class Solution:
    def countHomogenous(self, s: str) -> int:
        res, cnt, MOD = 0, 0, 10**9+7
        s += '$'
        for i, ch in enumerate(s):
            if i == 0 or s[i] == s[i-1]:
                cnt += 1
            else:
                res += cnt*(cnt+1)//2
                res %= MOD
                cnt = 1
        return res 

    def countHomogenous(self, s):
        res = 0
        for c, s in groupby(s):
            n = len(list(s))
            res += n * (n + 1) / 2
        return res % (10**9 + 7)