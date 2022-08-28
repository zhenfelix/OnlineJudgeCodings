class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        g = defaultdict(lambda :defaultdict(list))
        seen = set([0,firstPerson])
        for x, y, t in meetings:
            g[t][x].append(y)
            g[t][y].append(x)
        arr = sorted([(k,v) for k, v in g.items()])
        def bfs(q, tg):
            while q:
                nq = []
                for cur in q:
                    for nxt in tg[cur]:
                        if nxt not in seen:
                            seen.add(nxt)
                            nq.append(nxt)
                q = nq 
            return

        for k, v in arr:
            q = []
            for cur in v.keys():
                if cur in seen:
                    q.append(cur)
            bfs(q,v)
            
        return list(seen)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        mp = defaultdict(list)
        seen = set([0,firstPerson])
        for u, v, t in meetings:
            mp[t].append((u,v))

        for t in sorted(mp):
            graph = defaultdict(list)
            candidates = set()
            for u, v in mp[t]:
                graph[u].append(v)
                graph[v].append(u)
                if u in seen:
                    candidates.add(u)
                if v in seen:
                    candidates.add(v)
            def dfs(cur):
                for nxt in graph[cur]:
                    if nxt not in seen:
                        seen.add(nxt)
                        dfs(nxt)
                return

            for x in candidates:
                dfs(x)

        return list(seen)