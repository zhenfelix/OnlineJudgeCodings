class Solution:
    def minimumChanges(self, s: str, removes: int) -> int:
        n = len(s)
        g  =  [[inf]*n for _ in range(n)]
        cnt = [[0]*n  for _ in range(n)]
        for d in range(1,n+1):
            for sz in range(d+d,n+1,d):
                for i in range(n):
                    if i+sz > n: break
                    for k in range(sz//2):
                        if s[i+k] != s[i+(sz//d-k//d-1)*d+k%d]:
                            cnt[i][i+sz-1] += 1
            # print(cnt)
            for i in range(n):
                for j in range(i+d*2-1,n,d):
                    g[i][j] = min(g[i][j],cnt[i][j])
                    cnt[i][j]= 0
        # print(g)
        f = g[0][:]
        for _ in range(removes-1):
            for j in range(n)[::-1]:
                f[j] = inf
                for i in range(j):
                    f[j] = min(f[j],f[i]+g[i+1][j])
        return f[-1]
