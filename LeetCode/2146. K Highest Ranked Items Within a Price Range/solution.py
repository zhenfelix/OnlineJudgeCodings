drc = [(-1,0),(1,0),(0,-1),(0,1)]
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        sr, sc = start
        lo, hi = pricing
        res = []
        visited = set()
        pq = [(0,grid[sr][sc],sr,sc)]
        visited.add((sr,sc))
        while pq:
            dist, price, r, c = heapq.heappop(pq)
            if lo <= price <= hi:
                res.append([r,c])
            if len(res) >= k:
                return res 
            for dr, dc in drc:
                dr += r 
                dc += c 
                if 0 <= dr < n and 0 <= dc < m and grid[dr][dc] > 0 and (dr,dc) not in visited:
                    heapq.heappush(pq, (dist+1,grid[dr][dc],dr,dc))
                    visited.add((dr,dc))
        return res 



drc = [(-1,0),(1,0),(0,-1),(0,1)]
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        sr, sc = start
        lo, hi = pricing
        res = []
        visited = set()
        pq = deque([(0,grid[sr][sc],sr,sc)])
        visited.add((sr,sc))
        while pq:
            dist, price, r, c = pq.popleft()
            if lo <= price <= hi:
                res.append([dist,price,r,c])
            # if len(res) >= k:
            #     return res 
            for dr, dc in drc:
                dr += r 
                dc += c 
                if 0 <= dr < n and 0 <= dc < m and grid[dr][dc] > 0 and (dr,dc) not in visited:
                    pq.append((dist+1,grid[dr][dc],dr,dc))
                    visited.add((dr,dc))
        return [[r,c] for _,_,r,c in sorted(res)[:k]]
