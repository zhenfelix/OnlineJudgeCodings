class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n, m = len(targetGrid), len(targetGrid[0])
        colors = set([x for row in targetGrid for x in row])
        # print(colors)
        graph = defaultdict(set)
        bound = {x: [float('inf'),-float('inf'),float('inf'),-float('inf')] for x in colors}
        for i in range(n):
            for j in range(m):
                x = targetGrid[i][j]
                bound[x][0] = min(bound[x][0], i)
                bound[x][1] = max(bound[x][1], i)
                bound[x][2] = min(bound[x][2], j)
                bound[x][3] = max(bound[x][3], j)

        for i in range(n):
            for j in range(m):
                x = targetGrid[i][j]
                for c in colors:
                    if x == c: continue
                    if bound[c][0] <= i <= bound[c][1] and bound[c][2] <= j <= bound[c][3]:
                        graph[c].add(x)

        # print(graph)
        state = [0]*70
        def dfs(cur):
            state[cur] = 1
            for nxt in graph[cur]:
                if state[nxt] == 1:
                    return False
                if state[nxt] == 0:
                    if dfs(nxt) == False:
                        return False
            state[cur] = 2
        for x in colors:
            if state[x] == 0:
                if dfs(x) == False:
                    return False

        return True