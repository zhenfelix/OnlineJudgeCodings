class Solution:
    def rootCount(self, edges: List[List[int]], gl: List[List[int]], k: int) -> int:
        n = len(edges)+1
        below, above = [0]*n, [0]*n 
        guesses = set([(a,b) for a,b in gl])
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        def dfs(cur, parent):
            for nxt in g[cur]:
                if nxt == parent: continue
                dfs(nxt, cur)
                below[cur] += below[nxt]
                if (cur,nxt) in guesses:
                    below[cur] += 1
            return  
        def dfs2(cur, parent):
            for nxt in g[cur]:
                if nxt == parent: continue
                above[nxt] = above[cur]+below[cur]
                above[nxt] -= below[nxt]
                if (cur,nxt) in guesses:
                    above[nxt] -= 1
                if (nxt,cur) in guesses:
                    above[nxt] += 1
                dfs2(nxt, cur)
            return
        dfs(0,0)
        dfs2(0,0)
        ans = 0
        for i in range(n):
            if above[i]+below[i] >= k:
                ans += 1
        return ans 