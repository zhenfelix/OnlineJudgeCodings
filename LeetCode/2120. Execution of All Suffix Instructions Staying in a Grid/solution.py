class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        dirs = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
        sz = len(s)
        def dfs(idx):
            r, c = startPos
            cnt = 0
            for i in range(idx,sz):
                dr, dc = dirs[s[i]]
                r += dr 
                c += dc 
                if 0 <= r < n and 0 <= c < n:
                    cnt += 1
                else:
                    return cnt
            return cnt

        return [dfs(j) for j in range(sz)]