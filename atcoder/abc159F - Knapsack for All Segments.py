import sys 

# sys.stdin = open("input","r") 

from collections import *
from heapq import * 
from functools import *
from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc

n, s = list(map(int,input().split()))
arr = list(map(int,input().split()))

MOD = 998244353
ans = 0
dp = [0]*(s+1)
for i, a in enumerate(arr):
    if s == a:
        ans = (ans+(i+1)*(n-i))%MOD
    elif s > a:
        ans = (ans+dp[s-a]*(n-i))%MOD
    for j in range(a,s+1)[::-1]:            
        if j == a:
            dp[j] += i+1
        else:
            dp[j] += dp[j-a]
        dp[j] %= MOD 
print(ans)