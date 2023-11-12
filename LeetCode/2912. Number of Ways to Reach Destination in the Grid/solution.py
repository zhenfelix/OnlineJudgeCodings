from typing import *
import numpy as np 
MOD = 10**9+7
class Solution:
    def numberOfWays(self, n: int, m: int, k: int, source: List[int], dest: List[int]) -> int:
        mat = np.array([[n+m-4,n-1,m-1,0],[1,m-2,0,m-1],[1,0,n-2,n-1],[0,1,1,0]])
        sx, sy = source
        dx, dy = dest
        dp = [sx!=dx and sy!=dy, sx==dx and sy!=dy, sx!=dx and sy==dy, sx==dx and sy==dy]
        dp = np.array(dp,dtype=int)
        ans = np.eye(4,4,dtype=int)
        # ans = dp 
        cur = mat 
        while k:
            if k&1:
                ans = cur@ans 
                ans %= MOD 
            cur = cur@cur 
            cur %= MOD
            k >>= 1
        # for _ in range(k):
        #     dp = mat@dp
        #     dp %= MOD
        dp = (ans@dp)%MOD
        return int(dp[-1])