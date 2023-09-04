class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        mx = max(nums)
        primes = [1]*(mx+1)
        cnt = [0]*(mx+1)
        for f in range(2,mx+1):
            if primes[f] == 0: continue
            for x in range(f,mx+1,f):
                primes[x] = 0
                cnt[x] += 1
        n = len(nums)
        parent = list(range(n))
        sz = [1]*n 
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def connect(u,v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[rv] = ru
                sz[ru] += sz[rv]
            return  
        arr = [(cnt[v],-i) for i, v in enumerate(nums)]
        brr = [(v,-i) for i, v in enumerate(nums)]
        comb = [0]*n 
        visited = [0]*n 
        for v, i in sorted(arr):
            i = -i  
            visited[i] = 1
            if i-1 >= 0 and visited[i-1]:
                connect(i-1,i)
            if i+1 < n and visited[i+1]:
                connect(i,i+1)
            left = find(i)
            tot = sz[left]
            comb[i] = (i-left+1)*(tot-(i-left))%MOD 
        ans = 1
        # print(arr,comb)
        for v, i in sorted(brr, reverse = True):
            if k <= 0: break 
            i = -i
            delta = comb[i] if k >= comb[i] else k 
            k -= delta
            # print(v,delta)
            ans = (ans*pow(v,delta,MOD))%MOD 
        return ans 



