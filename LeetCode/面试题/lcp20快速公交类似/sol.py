from collections import *
from functools import *

def solve():
    n, k = list(map(int,input().split()))
    @lru_cache(None)
    def dfs(cur):
        if cur <= k or cur <= 1:
            return abs(k-cur) 
        ans = cur-k 
        if cur%2 == 0:
            return min(dfs(cur//2)+1,ans)
        return min(dfs(cur//2)+2,dfs(cur//2+1)+2,ans)
    return dfs(n)


print(solve())