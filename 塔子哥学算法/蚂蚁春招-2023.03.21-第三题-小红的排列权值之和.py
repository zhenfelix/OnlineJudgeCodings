n = int(input())
m = (n+1)//2
MOD = 10**9+7
f = [1]*(n+1)
for i in range(n):
    f[i+1] = ((i+1)*f[i])%MOD
print((f[n-1]*m*(m-1))%MOD)