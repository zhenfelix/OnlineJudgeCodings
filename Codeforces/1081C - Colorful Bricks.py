import sys 

sys.stdin = open("input","r") 

MOD = 998244353
n, m, k = list(map(int, input().split()))

dp = [0]*(k+1)
dp[0] = m 
for _ in range(n-1):
    for j in range(1,k+1)[::-1]:
        dp[j] += dp[j-1]*(m-1)
        dp[j] %= MOD
print(dp[-1])