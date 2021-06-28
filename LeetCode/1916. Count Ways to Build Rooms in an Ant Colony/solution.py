def quick_mul(a, p):
    ans = 1
    while p:
        if p&1:
            ans *= a 
            ans %= MOD 
        a *= a 
        a %= MOD 
        p = (p>>1)
    return ans 

n = 10**5+5
MOD = 10**9+7

factors = [1]*n 
rev_factors = [1]*n
for i in range(1,n):
    factors[i] = i*factors[i-1]%MOD
# for i in range(1,n):
#     rev_factors[i] = quick_mul(factors[i], MOD-2)%MOD 

rev_factors[n-1] = pow(factors[n-1], MOD-2, MOD) 
for i in range(1,n-1)[::-1]:
    # rev_factors[i] = quick_mul(factors[i], MOD-2)%MOD 
    rev_factors[i] = rev_factors[i+1]*(i+1)%MOD

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        
        graph = defaultdict(list)
        for cur, pre in enumerate(prevRoom):
            if pre >= 0:
                graph[pre].append(cur)

        

      
        def dfs(room):
            res, tot = 1 , 0
            for nxt in graph[room]:
                path, sz = dfs(nxt)
                tot += sz 
                res *= path
                res *= rev_factors[sz]
                res %= MOD
            res *= factors[tot]
            res %= MOD
            # print(fac, tot, tot2)
            
            return res, tot+1

        return dfs(0)[0]




class Solution:
    def waysToBuildRooms(self, arr: int) -> int:
        MOD = 10**9 + 7
        g = collections.defaultdict(list)
        for cur, pre in enumerate(arr):
            g[pre].append(cur)
            
        def dfs(cur):
            if not g[cur]:
                return 1, 1
            ans, l = 1, 0
            for nxt in g[cur]:
                tmp, r = dfs(nxt)
                ans = (ans * tmp * math.comb(l+r, r)) % MOD
                l += r
            return ans, l + 1
            
        return dfs(0)[0]



from math import comb
from functools import reduce


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9+7
        graph = defaultdict(list)
        for cur, pre in enumerate(prevRoom):
            if pre >= 0:
                graph[pre].append(cur)
      
        def dfs(room):
            res = 1 
            child = []
            for nxt in graph[room]:
                path, sz = dfs(nxt)
                child.append(sz)
                res *= path
                res %= MOD
            tot2 = tot = sum(child)
            for sz in child:
                res *= comb(tot,sz)
                res %= MOD
                tot -= sz
            # print(fac, tot, tot2)
            
            return res, tot2+1

        return dfs(0)[0]

