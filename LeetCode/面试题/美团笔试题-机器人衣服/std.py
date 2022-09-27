from collections import *
from functools import *

def solve():
    n, B = list(map(int,input().split()))
    ts = list(map(int,input().split()))
    ps = list(map(int,input().split()))

    @lru_cache(None)
    def dfs(i,w):
        res = float('inf')
        if w < ps[i]:
            return res 
        res = (n-i)*ts[i]
        for j in range(i+1,n):
            res = min(res, max((j-i)*ts[i], dfs(j,w-ps[i])))
        return res 
    ans = dfs(0,B)
    return ans if ans < float('inf') else -1


print(solve())