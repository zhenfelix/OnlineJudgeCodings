import sys, os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, k = map(int, input().split())
mod = 998244353
dp0 = [0] * (n + 1)
dp0[0] = 1
dp1 = [0] * (n + 1)
ans = [0] * n
c = 0
while c < n:
    for i in range(c, n + 1 - k):
        dp1[i + k] += (dp0[i] + dp1[i]) % mod
        dp1[i + k] %= mod
    dp0 = dp1
    dp1 = [0] * (n + 1)
    for i in range(c, n + 1):
        ans[i - 1] += dp0[i]
        ans[i - 1] %= mod
    c += k
    k += 1
sys.stdout.write(" ".join(map(str, ans)))