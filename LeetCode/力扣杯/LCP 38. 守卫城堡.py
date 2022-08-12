class Solution:
    def guardCastle(self, grid: List[str]) -> int:
        n = len(grid[0])
        mp = {'.':0, 'C':1, 'S':2, '#':3}
        def catch(x, y):
            if (x == 1 or x == 2) and x + y == 3:
                return True
            return False

        def check(g):
            dp = [[inf]*4 for _ in range(4)]
            dp[0][0] = 0
            for i in range(n):
                ndp = [[inf]*4 for _ in range(4)]
                s0, s1 = mp[g[0][i]], mp[g[1][i]]

                def update(t0,t1,s0,s1,extra):
                    if catch(t0,t1) or catch(t0,s0) or catch(t1,s1):
                        return
                    if s0 == 0 and t0 < 3:
                        s0 = t0
                    if s1 == 0 and t1 < 3:
                        s1 = t1
                    if catch(s0,s1):
                        return
                    if s0 == 0 and s1 < 3:
                        s0 = s1
                    if s1 == 0 and s0 < 3:
                        s1 = s0
                    ndp[s0][s1] = min(ndp[s0][s1], dp[t0][t1]+extra)
                    return

                for t0 in range(4):
                    for t1 in range(4):
                        if dp[t0][t1] == inf:
                            continue
                        # important pruning to AC python code
                        update(t0,t1,s0,s1,0)
                        if g[0][i] == '.':
                            update(t0,t1,3,s1,1)
                        if g[1][i] == '.':
                            update(t0,t1,s0,3,1)
                        if g[0][i] == '.' and g[1][i] == '.':
                            update(t0,t1,3,3,2)
                dp = ndp
            return min(map(min,dp))

        ans = inf 
        g1 = [[None]*n for _ in range(2)]
        for i in range(2):
            for j in range(n):
                if grid[i][j] == 'P':
                    g1[i][j] = 'C'
                else:
                    g1[i][j] = grid[i][j]
        ans = min(ans, check(g1))
        g2 = [[None]*n for _ in range(2)]
        for i in range(2):
            for j in range(n):
                if grid[i][j] == 'P':
                    g2[i][j] = 'S'
                else:
                    g2[i][j] = grid[i][j]
        ans = min(ans, check(g2))
        if ans == inf:
            return -1
        return ans 







class Solution:
    def guardCastle(self, grid: List[str]) -> int:
        def merge(x1, x2, y1, y2):
            x1 = y1 if y1+x1 in ['C.', 'S.'] else x1
            x2 = y2 if y2+x2 in ['C.', 'S.'] else x2
            x1 = x2 if x1+x2 in ['.C', '.S'] else x1 
            x2 = x1 if x1+x2 in ['C.', 'S.'] else x2 
            if x1+y1 in ['CS', 'SC'] or x2+y2 in ['CS', 'SC']:
                return 'CS'
            return x1+x2

        def cal(grid):
            d = {'..': 0}
            for a1, a2 in zip(*grid):
                if not d:
                    return float('inf')
                new = defaultdict(lambda: float('inf'))
                for x1, x2, w in [(a1, a2, 0), (a1, '#', 1), ('#', a2, 1), ('#', '#', 2)]:
                    if a1+x1 in ['S#', 'C#'] or a2+x2 in ['S#', 'C#']:
                        continue 
                    for y, w2 in d.items():
                        cur = merge(x1, x2, y[0], y[1])
                        if cur not in ['SC', 'CS']:
                            new[cur] = min(new[cur], w+w2)
                d = new
            return min(d.values(), default=float('inf'))
        
        grid1 = [row.replace('P', 'C') for row in grid]
        grid2 = [row.replace('P', 'S') for row in grid]
        res = min(cal(grid1), cal(grid2))
        return res if res<float('inf') else -1
