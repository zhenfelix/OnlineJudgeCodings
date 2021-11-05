dxy = [[-1,0],[1,0],[0,-1],[0,1]]

class Solution:
    def bicycleYard(self, position: List[int], terrain: List[List[int]], obstacle: List[List[int]]) -> List[List[int]]:
        q = deque()
        seen = set()
        res = []
        r, c = position
        q.append((r,c,1))
        seen.add((r,c,1))
        n, m = len(terrain), len(terrain[0])
        while q:
            r, c, s = q.popleft()
            if s == 1 and [r,c] != position:
                res.append([r,c])
            for dr, dc in dxy:
                dr += r 
                dc += c  
                if dr < 0 or dr >= n or dc < 0 or dc >= m:
                    continue
                ss = s + terrain[r][c] - terrain[dr][dc] - obstacle[dr][dc]
                if ss <= 0:
                    continue
                if (dr,dc,ss) not in seen:
                    q.append((dr,dc,ss))
                    seen.add((dr,dc,ss))
        return sorted(res)
