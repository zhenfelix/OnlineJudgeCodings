from functools import *
from math import *
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        arr = [i for i in range(n) if s1[i] != s2[i]]
        m = len(arr)
        if m%2: return -1
        @lru_cache(None)
        def dfs(i,s):
            if i >= m: return 0 if s == 0 else inf 
            ans = inf 
            if s: ans = min(ans, dfs(i+1,0))
            if i < m-1: ans = min(ans, arr[i+1]-arr[i]+dfs(i+2,s))
            if s == 0: ans = min(ans, x+dfs(i+1,1))
            return ans 
        return dfs(0,0)

class Solution2:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        arr = [i for i in range(n) if s1[i] != s2[i]]
        m = len(arr)
        if m%2: return -1
        @lru_cache(None)
        def dfs(i,j):
            if i > j: return 0 
            return min(dfs(i+1,j-1)+x,dfs(i+2,j)+arr[i+1]-arr[i],dfs(i,j-2)+arr[j]-arr[j-1])
        return dfs(0,m-1)
    

import random
for _ in range(1):
    n = random.randint(1,500)
    # s1 = ''.join(random.choices("01",k=n))
    # s2 = ''.join(random.choices("01",k=n))
    # x = random.randint(1,2)
    x = 2
    s1 = "10000000001000011110001000000001"
    s2 = "00000000000000000000000000000000"
    Sol = Solution()
    Sol2 = Solution2()
    assert(Sol.minOperations(s1,s2,x) == Sol2.minOperations(s1,s2,x))