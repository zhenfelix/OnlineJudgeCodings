class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = inf  
        for i in range(n):
            dist = [inf]*n 
            dist[i] = 0
            q = deque()
            q.append(i)
            parent = [-1]*n 
            flag = True
            while q and flag:
                cur = q.popleft()
                for nxt in g[cur]:
                    if dist[nxt] == inf:
                        q.append(nxt)
                        dist[nxt] = dist[cur]+1
                        parent[nxt] = cur
                    elif parent[cur] != nxt:
                        ans = min(ans, dist[cur]+dist[nxt]+1)
                        flag = False
                        # break
                        # without commenting break, solution will fail on this testcase
# 9
# [[0,1],[1,6],[6,2],[2,3],[3,7],[7,4],[4,5],[5,8],[8,0],[8,6],[6,7],[7,8]]
        return ans if ans < inf else -1