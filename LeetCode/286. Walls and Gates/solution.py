from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        n, m = len(rooms), len(rooms[0])
        q = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q.append((i,j,0))
                    visited.add((i,j))

        while q:
            i, j, dis = q.popleft()
            if i < 0 or i >= n or j < 0 or j >= m or rooms[i][j] == -1:
                continue
            rooms[i][j] = min(rooms[i][j], dis)
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                if (i+dx,j+dy) not in visited:
                    q.append((i+dx,j+dy,dis+1))
                    visited.add((i+dx,j+dy))
        return