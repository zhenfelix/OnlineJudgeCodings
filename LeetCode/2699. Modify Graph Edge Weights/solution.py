class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        sz = [1]*n 
        # g = defaultdict(list)
        # for a, b in edges:
        #     g[a].append(b)
        #     g[b].append(a)
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def connect(u,v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv 
                sz[rv] += sz[ru]
            return  
        for a, b in edges:
            connect(a,b)
        groups = set()
        cnt = [0]*n 
        seen = set()
        for a, b in edges:
            seen.add(a)
            seen.add(b)
            j = find(a)
            groups.add((j,sz[j]))
            cnt[j] += 1
            
        ans = n-len(seen)
        for j, s in groups:
            # print(j,s,cnt[j])
            if s*(s-1)//2 == cnt[j]:
                ans += 1
        return ans 