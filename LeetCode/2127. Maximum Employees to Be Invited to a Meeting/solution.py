class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        dp = [1]*n
        cc = Counter(favorite)
        q = deque([i for i in range(n) if cc[i] == 0])
        while q:
            cur = q.popleft()
            nxt = favorite[cur]
            dp[nxt] = max(dp[nxt], dp[cur]+1)
            cc[nxt] -= 1
            if cc[nxt] == 0:
                q.append(nxt)

        visited = [False]*n 
        def dfs(cur):
            visited[cur] = True
            nxt = favorite[cur]
            if visited[nxt]:
                return True, 1
            flag, depth = dfs(nxt)
            return flag, depth+1

        ans, bi = 0, 0
        for i in range(n):
            if cc[i] and not visited[i]:
                _, cnt = dfs(i)
                if cnt == 2:
                    bi += dp[i]+dp[favorite[i]]
                else:
                    ans = max(ans, cnt)
        return max(ans,bi) 





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