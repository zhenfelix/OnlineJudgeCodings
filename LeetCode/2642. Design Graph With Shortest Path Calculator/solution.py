class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = defaultdict(list)
        self.n = n 
        for a,b,c in edges:
            self.g[a].append((b,c))


    def addEdge(self, edge: List[int]) -> None:
        a,b,c = edge
        self.g[a].append((b,c))


    def shortestPath(self, start: int, end: int) -> int:
        n = self.n 
        g = self.g 
        dist = [inf]*n 
        dist[start] = 0 
        hq = [(0,start)]
        while hq:
            d, cur = heappop(hq)
            if cur == end:
                return d 
            if d > dist[cur]: continue
            for nxt, c in g[cur]:
                if d+c < dist[nxt]:
                    dist[nxt] = d+c 
                    heappush(hq,(dist[nxt],nxt))
        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

