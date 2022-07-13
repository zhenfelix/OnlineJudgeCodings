MOD = 10**9+7
N, M = 15, 10000
dp = [[0]*M for _ in range(N)]
for i in range(M):
    dp[0][i] = 1
for i in range(1,N):
    for a in range(1,M+1):
        if a*a > M:
            break    
        for b in range(a,M+1):
            if b*a > M:
                break
            if a*b != a:
                dp[i][a*b-1] += dp[i-1][a-1]
            if a != b and a*b != b:
                dp[i][a*b-1] += dp[i-1][b-1]
            dp[i][a*b-1] %= MOD
# for i in range(5):
#     print(dp[i][:10])

T, i = N, 10000
cb = [[0]*(T+1) for _ in range(i+1)]
for i in range(i+1):
    cb[i][0] = 1
for i in range(1,i+1):
    for j in range(1,T+1):
        if j > i:
            break
        cb[i][j] = (cb[i-1][j] + cb[i-1][j-1])%MOD
# for _ in range(5):
#     print(cb[_][:]) 

class Solution:
    def idealArrays(self, n: int, m: int) -> int:
        ans = 0
        for i in range(min(n,N)):
            cur = sum(dp[i][j] for j in range(m))%MOD
            # print(i+1, cur)
            cur = (cur*cb[n-1][min(i,n-1)])%MOD
            # print(i+1, n-1, i, cb[n-1][min(i,n-1)])
            ans = (ans+cur)%MOD
        return ans
        


# TLE
# class Solution:
#     def idealArrays(self, n: int, maxaalue: int) -> int:
#         MOD = 10**9+7
#         dp = [1]*maxaalue
#         for _ in range(n-1):
#             ndp = [0]*maxaalue
#             a = 1
#             while a*a <= maxaalue:
#                 i = a
#                 ndp[a*i-1] += dp[a-1]
#                 ndp[a*i-1] %= MOD
#                 while a*(i+1) <= maxaalue:
#                     i += 1 
#                     ndp[a*i-1] += dp[a-1]+dp[i-1]
#                     ndp[a*i-1] %= MOD
#                 a += 1
#             dp = ndp
#         return sum(ndp)%MOD
