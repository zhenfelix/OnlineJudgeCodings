class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        MAX_N = 100001
        spf = list(range(MAX_N))
        i = 2
        while i * i < MAX_N:
            if spf[i] == i:
                for j in range(i * i, MAX_N, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1
        
        def get_sf(k):
            res = 1
            while k > 1:
                p = spf[k]
                c = 0
                while k % p == 0:
                    c += 1
                    k //= p
                if c % 2 == 1:
                    res *= p
            return res
            
        sf_vals = [get_sf(x) for x in nums]
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        ans = 0
        counts = collections.defaultdict(int)
        
        def dfs(u, p):
            nonlocal ans
            
            v = sf_vals[u]
            ans += counts[v]
            
            counts[v] += 1
            for neighbor in adj[u]:
                if neighbor != p:
                    dfs(neighbor, u)
            counts[v] -= 1
        
        dfs(0, -1)
        return ans