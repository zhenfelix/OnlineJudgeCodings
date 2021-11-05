class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = defaultdict(list)
        for i, p in enumerate(parents):
            if p != -1:
                graph[p].append(i)
        n = len(parents)
        score = [1]*n 
        sz = [1]*n  

        def dfs(cur):
            tot = n-1
            for nxt in graph[cur]:
                dfs(nxt)
                sz[cur] += sz[nxt]
                score[cur] *= sz[nxt]
                tot -= sz[nxt]
            if tot > 0:
                score[cur] *= tot
                
        dfs(0)
        mx = max(score)
        # print(score,sz)
        return sum(s == mx for s in score)

