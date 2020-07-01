# class Solution:
#     def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
#         for i, e in enumerate(edges):
#             edges[i].append(i)
#         edges.sort(key=lambda x:x[-2])
        
#         # print(edges)
#         parent = [i for i in range(n)]
#         def find(cur):
#             if cur == parent[cur]:
#                 return cur 
#             return find(parent[cur])

#         A, B = set([i for i in range(len(edges))]), set()
#         res = []
#         def dfs(idx, st):
#             nonlocal A,B
#             # print(res,st)
#             if res and edges[st[-1]][-2] > edges[res[-1][len(st)-1]][-2]:
#                 return 
#             if len(st) == n-1:
#                 res.append(st)
#                 st = set(st)
#                 A &= st 
#                 B |= st 
#                 # print(st,minsums)
#                 # print(A,B)
#                 return 
#             cur = float(inf)
#             while idx < len(edges):
#                 a, b, w, _ = edges[idx]
#                 ra, rb = find(a), find(b)
#                 if ra != rb and w <= cur:
#                     cur = w 
#                     parent[ra] = rb
#                     dfs(idx+1, st+[idx])
#                     parent[ra] = ra 
#                 idx += 1
#             return True
#         dfs(0,[])
#         # print(mp)
#         # print(A,B)
        
#         return [list(map(lambda x: edges[x][-1],list(A))),list(map(lambda x: edges[x][-1],list(B-A)))]




class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def find(cur):
            if cur != parent[cur]:
                parent[cur] = find(parent[cur])
            return parent[cur]

        def union(a,b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb 
                return True
            return False

        def MST(jump, total):
            sums, cnt = 0, 0
            for i in range(len(edges)):
                if i in jump: continue
                a, b, w, _ = edges[i]
                f = union(a,b)
                cnt += f
                sums += f*w 
                if cnt == total: break
            return sums if cnt == total else float('inf')

        edges = [edge+[i] for i, edge in enumerate(edges)]
        # print(edges)
        edges.sort(key=lambda x: x[-2])
        parent = [i for i in range(n)]
        target = MST([],n-1)
        # print(target)
        A, B = [], []
        for i in range(len(edges)):
            u,v,w,pos = edges[i]
            parent = [i for i in range(n)]
            cur = MST([i],n-1)
            # print(cur)
            if cur > target:
                A.append(pos)
            else:
                parent = [i for i in range(n)]
                union(u,v)
                cur = MST([i],n-2)
                if cur+w == target:
                    B.append(pos)
        return [A,B]












class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [e+[i] for i,e in enumerate(edges)]
        edges.sort(key = lambda x:x[-2])
        edges.append([-1,-1,float('inf'),-1])
        parent = [i for i in range(n)]
        pre = 0
        g = defaultdict(list)
        vs = set()
        tmp = []
        a, b = [], []

        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
            return

        def dfs(cur,d):
            # print(cur,d)
            if rank[cur] > 0: return
            rank[cur] = d 
            for nxt, idx in g[cur]:
                if idx in visited: continue
                visited.add(idx)
                dfs(nxt,d+1)
                rank[cur] = min(rank[cur],rank[nxt])
                if d < rank[nxt]:
                    a.append(idx)
                else:
                    b.append(idx)
            return


        for u, v, w, i in edges:
            
            if w != pre:
                rank = defaultdict(int)
                depth = 0
                # print(u,v,w,i)
                # print(vs,g)
                visited = set()
                for x in vs:
                    dfs(x,1)
                # print(a,b)
                for ru, rv in tmp:
                    union(ru, rv)
                g = defaultdict(list)
                vs = set()
                tmp = []
            if w == float('inf'): break
            ru, rv = find(u), find(v)
            if ru == rv: continue
            g[ru].append((rv,i))
            g[rv].append((ru,i))
            vs.add(ru)
            vs.add(rv)
            tmp.append((ru,rv))
            pre = w

        return [a,b]




class UnionFindSet:
    def __init__(self, n=0):
        self.parents = {}
        self.ranks = {}
        self.count = 0
        for i in range(n):
            self.add(i)

    def add(self, p):
        self.parents[p] = p
        self.ranks[p] = 1
        self.count += 1

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: 
            return False
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:        
            self.parents[pv] = pu
            self.ranks[pu] += 1
        self.count -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    
        # reference: LC 1192
        def dfs(curr, level, parent):
            levels[curr] = level
            for child, i in graph[curr]:
                if child == parent:
                    continue
                elif levels[child] == -1:
                    levels[curr] = min(levels[curr], dfs(child, level + 1, curr))
                else:
                    levels[curr] = min(levels[curr], levels[child])
                if levels[child] >= level + 1 and i not in p_cri:
                    cri.add(i)
            return levels[curr]
        
        # init critical and pseudo-critical edge set
        cri, p_cri = set(), set()
        
        # use dic to store all edges associated with a given weight
        dic = collections.defaultdict(list)
        for i, (u, v, w) in enumerate(edges):
            dic[w].append([u, v, i])
        
        # define union find et
        union_set = UnionFindSet(n)
        
        # iterate through all weights in ascending order
        for w in sorted(dic):
                
            # seen[(pu, pv)] contains all edges connecting pu and pv,
            # where pu and pv are the parent nodes of their corresponding groups
            seen = collections.defaultdict(set)
            # populate seen
            for u, v, i in dic[w]:
                pu, pv = union_set.find(u), union_set.find(v)
                # skip the edge that creates cycle
                if pu == pv:
                    continue
                seen[min(pu, pv), max(pu, pv)].add(i) # edge i connects pu and pv
            
            # w_edges contains all weight-w edges we may add to MST
            w_edges, graph = [], collections.defaultdict(list)
            for pu, pv in seen:
                # more than 1 edge can connect pu and pv
                # these edges are pseudo-critical
                if len(seen[pu, pv]) > 1:
                    p_cri |= seen[pu, pv]
                # construct graph for weight w 
                edge_idx = seen[pu, pv].pop()
                graph[pu].append((pv, edge_idx))
                graph[pv].append((pu, edge_idx))
                w_edges.append((pu, pv, edge_idx))
                # union pu and pv groups
                union_set.union(pu, pv)
            
            # run dfs to mark all critical w_edges
            levels = [-1] * n
            for u, v, i in w_edges:
                if levels[u] == -1:
                    dfs(u, 0, -1)
            # the edges in w_edges cycles are pseudo-critical
            for u, v, i in w_edges:
                if i not in cri:
                    p_cri.add(i)
        
        return [cri, p_cri]