class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        # print(n)
        # if n <= 3:
        #     return n 
        visited = [False]*n
        depth = [0]*n
        def dfs(cur, d):
            depth[cur] = d 
            nxt = favorite[cur]
            if visited[nxt]:
                visited[cur] = True
                return 0
            elif depth[nxt] > 0:
                visited[cur] = True
                return depth[cur]-depth[nxt]+1
            else:
                res = dfs(nxt, d+1)
                visited[cur] = True
                return res
        mx = 0
        for i in range(n):
            if not visited[i]:
                mx = max(mx, dfs(i,1))
        # print(mx)
        
        
        children = defaultdict(list)
        for cur, nxt in enumerate(favorite):
            children[nxt].append(cur)
        visited = [False]*n 
        def dfs2(cur):
            cnt = 1
            for nxt in children[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    cnt = max(cnt, dfs2(nxt)+1)
            return cnt
        mx2 = 0
        # units = 0
        for i in range(n):
            if not visited[i] and not visited[favorite[i]] and i == favorite[favorite[i]]:
                visited[i] = True
                visited[favorite[i]] = True
                mx2 += dfs2(i)+dfs2(favorite[i])

        return max(mx,mx2)