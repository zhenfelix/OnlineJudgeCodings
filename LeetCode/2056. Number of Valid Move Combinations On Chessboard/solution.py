class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        diag = [(-1,-1),(1,1),(-1,1),(1,-1)]
        lines = [(0,1),(1,0),(-1,0),(0,-1)]
        n = len(pieces)
        res = 0

        def check(path):
            cur = [[r,c] for r,c in positions]
            des = [[positions[i][0]+path[i][0]*path[i][-1], positions[i][1]+path[i][1]*path[i][-1]] for i in range(n)]
            for t in range(8):
                for i, (dr,dc,dt) in enumerate(path):
                    if cur[i] == des[i]:
                        continue
                    cur[i][0] += dr
                    cur[i][1] += dc
                for i in range(n):
                    for j in range(i+1,n):
                        if cur[i] == cur[j]:
                            return False
                if all(cur[i] == des[i] for i in range(n)):
                    break
            return True


        def dfs(i, path):
            nonlocal res
            if i == n:
                if check(path):
                    res += 1
                return
            r, c = positions[i]
            dfs(i+1, path+[(0,0,0)])
            if pieces[i] in ["rook","queen"]:
                for dr, dc in lines:
                    for t in range(1,8):
                        if r+t*dr > 8 or r+t*dr < 1 or c+t*dc > 8 or c+t*dc < 1:
                            break
                        dfs(i+1, path+[(dr,dc,t)])
            if pieces[i] in ["bishop","queen"]:
                for dr, dc in diag:
                    for t in range(1,8):
                        if r+t*dr > 8 or r+t*dr < 1 or c+t*dc > 8 or c+t*dc < 1:
                            break
                        dfs(i+1, path+[(dr,dc,t)])
            return

        dfs(0,[])
        return res

