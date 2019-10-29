from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        edges = defaultdict(set)
        mp = defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                for pre in mp[stop]:
                    edges[pre].add(bus)
                    edges[bus].add(pre)
                mp[stop].add(bus)

        q = deque()
        visited = set()
        for start in mp[S]:
            q.append(start)
            visited.add(start)
        res = 1
        while q:
            n = len(q)
            for _ in range(n):
                bus = q.popleft()
                if bus in mp[T]:
                    return res
                for nxt in edges[bus]:
                    if nxt not in visited:
                        q.append(nxt)
                        visited.add(nxt)
            res += 1
        return -1
            

