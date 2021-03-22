class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            cnt = Counter()
            mx, mi = 0, 0
            for j in range(i,n):
                ch = s[j]
                cnt[ch] += 1
                mx = max(cnt.values())
                mi = min(cnt.values())
                # print(i,j,mi,mx,cnt)
                res += mx-mi
        return res 