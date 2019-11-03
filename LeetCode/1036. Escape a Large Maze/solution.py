class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set([tuple(x) for x in blocked])
        def bfs(start):
            q = collections.deque()
            visited = set()
            q.append(start)
            visited.add(start)
            cnt = len(blocked)**2
            while q and cnt:
                x, y = q.popleft()
                cnt -= 1
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    xx, yy = x+dx, y+dy
                    if xx < 0 or xx >= 10**6 or yy < 0 or yy >= 10**6 or (xx,yy) in blocked:
                        continue
                    if (xx,yy) not in visited:
                        q.append((xx,yy))
                        visited.add((xx,yy))
            return len(q) == 0
        f1 = bfs(tuple(source))
        f2 = bfs(tuple(target))
        # print(f1,f2)
        return not (f1^f2)


