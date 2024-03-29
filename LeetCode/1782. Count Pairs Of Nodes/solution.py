class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        cc = [0]*n 
        ec = Counter()
        g = defaultdict(set)
        for u, v in edges:
            u -= 1
            v -= 1
            cc[u] += 1
            cc[v] += 1
            g[u].add(v)
            g[v].add(u)
            ec[u,v] += 1
            ec[v,u] += 1
        nodes = list(range(n))
        nodes.sort(key = lambda x: cc[x])
        ans = []
        for q in queries:
            cnt = 0
            j = n-1
            for i in range(n):
                while j >= 0 and cc[nodes[i]]+cc[nodes[j]] > q:
                    j -= 1
                cnt += n-1-j
                if j < i:
                    cnt -= 1

                for k in g[nodes[i]]:
                    if cc[nodes[i]]+cc[k]-ec[nodes[i],k] > q:
                        cnt += 1
                    if cc[nodes[i]]+cc[k] > q:
                        cnt -= 1
            ans.append(cnt//2)
        return ans 
                    
        
        
        


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        cc = [0]*n 
        ec = Counter()
        g = defaultdict(set)
        for u, v in edges:
            u -= 1
            v -= 1
            cc[u] += 1
            cc[v] += 1
            g[u].add(v)
            g[v].add(u)
            ec[u,v] += 1
            ec[v,u] += 1
        nodes = list(range(n))
        nodes.sort(key = lambda x: cc[x])
        ans = []
        for q in queries:
            cnt = 0
            j = n-1
            left, right = set(), set()
            for i in range(n):
                while j > i and cc[nodes[i]]+cc[nodes[j]] > q:
                    right.add(nodes[j])
                    j -= 1
                if j < i:
                    j += 1
                    right.remove(nodes[j])
                    
                cnt += n-1-j

                for k in g[nodes[i]]:
                    if k in left: continue
                    if k in right: 
                        cnt -= 1
                    if cc[nodes[i]]+cc[k]-ec[nodes[i],k] > q:
                        cnt += 1
                left.add(nodes[i])
            ans.append(cnt)
        return ans 
                    
        
        
        
        

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = Counter()
        ecnt = Counter()
        for u, v in edges:
            u -= 1
            v -= 1
            degree[u] += 1
            degree[v] += 1
            ecnt[min(u,v),max(u,v)] += 1
        # edges = set([(min(u,v),max(u,v)) for u, v in edges])
        arr = sorted([degree[i] for i in range(n)])
        # print(arr,edges)
        ans = []
        for q in queries:
            left, right = 0, n-1
            cnt = 0
            while left < n:
                while left < right and arr[left]+arr[right] > q:
                    right -= 1
                cnt += n-1-max(left,right)
                # print(left,right,cnt)
                left += 1
            
            # print(q,cnt)
            for u, v in ecnt:
                # print(u,v,ecnt[u,v])
                if q < degree[u] + degree[v] <= q + ecnt[u,v]:
                    cnt -= 1
            ans.append(cnt)
        return ans


# class Solution:
#     def update(self,tree,m,x,delta):
#         while x <= m:
#             tree[x] += delta
#             x += x&(-x)
#     def query(self,tree,m,x):
#         sums = 0
#         while x > 0:
#             sums += tree[x]
#             x -= x&(-x)
#         return sums
            
#     def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
#         degree = Counter()
#         ecnt = Counter()
#         g = defaultdict(set)
#         ans = [0]*len(queries)
#         for u, v in edges:
#             u -= 1
#             v -= 1
#             degree[u] += 1
#             degree[v] += 1
#             ecnt[min(u,v),max(u,v)] += 1

#             g[u].add(v)
#             g[v].add(u)

#         m = len(edges)
#         # m = max(degree.values())
#         tree = [0]*(m+2)
#         for i in range(n):
#             self.update(tree,m+1,degree[i]+1,1)
#         # print(tree)

#         for i, cnt in enumerate(queries):
#             sums = 0
#             for cur in range(n):
#                 for nxt in g[cur]:
#                     self.update(tree,m+1,degree[nxt]+1,-1)
#                     if degree[cur]+degree[nxt]-ecnt[min(cur,nxt),max(cur,nxt)] > cnt:
#                         sums += 1
#                 self.update(tree,m+1,degree[cur]+1,-1)
#                 sums += self.query(tree,m+1,m+1)-self.query(tree,m+1,max(0,cnt-degree[cur]+1))
#                 for nxt in g[cur]:
#                     self.update(tree,m+1,degree[nxt]+1,1)
#                 self.update(tree,m+1,degree[cur]+1,1)
#             ans[i] = sums//2
#         return ans 





