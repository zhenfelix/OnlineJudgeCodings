class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def dfs(tree,dp,cur,pre):
            for nxt in tree[cur]:
                if pre == nxt: continue
                dfs(tree,dp,nxt,cur)
                if dp[nxt][0]+1 > dp[cur][0]:
                    dp[cur][1] = dp[cur][0]
                    dp[cur][0] = dp[nxt][0]+1
                elif dp[nxt][0]+1 > dp[cur][1]:
                    dp[cur][1] = dp[nxt][0]+1
            return

        def dfs2(tree,dp,mx,cur,pre,up):
            mx[cur] = max(dp[cur][0],up)
            for nxt in tree[cur]:
                if pre == nxt: continue
                d = dp[nxt][0]+1
                tmp = up
                if d == dp[cur][0]:
                    tmp = max(tmp,dp[cur][1])
                else:
                    tmp = max(tmp,dp[cur][0])
                dfs2(tree,dp,mx,nxt,cur,tmp+1)
            return

        tree1 = defaultdict(list)
        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        n = len(edges1)+1
        dp1 = [[0]*2 for _ in range(n)]
        mx1 = [0]*n 
        dfs(tree1,dp1,0,0)
        dfs2(tree1,dp1,mx1,0,0,0)

        tree2 = defaultdict(list)
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
        m = len(edges2)+1
        dp2 = [[0]*2 for _ in range(m)]
        mx2 = [0]*m 
        dfs(tree2,dp2,0,0)
        dfs2(tree2,dp2,mx2,0,0,0)
        # print(tree1,tree2)
        # print(dp1,dp2)
        # print(mx1,mx2)

        return max(max(mx1),max(mx2),min(mx1)+min(mx2)+1)
            
            
