class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = "NSEW"
        dxy = [[0,-1],[0,1],[1,0],[-1,0]]
        mp = {ch: i for i, ch in enumerate(s)}
        path = [mp[ch] for ch in path]
        x, y = 0, 0
        seen = set()
        seen.add((0,0))
        for i in path:
            dx, dy = dxy[i]
            x += dx 
            y += dy 
            if (x,y) in seen:
                return True
            seen.add((x,y))
        return False