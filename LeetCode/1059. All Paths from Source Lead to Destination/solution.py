from collections import defaultdict

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # @functools.lru_cache(None)
        def dfs(node, visited):
            # print(node, visited)
            if node in memo:
                return memo[node]
            
            if node == destination:
                memo[node] = len(graph[node]) == 0
                return memo[node]
            
            if node in visited or len(graph[node]) == 0:
                memo[node] = False
                return False
            

            visited.append(node)
            for nxt in graph[node]:
                if not dfs(nxt, visited):
                    memo[node] = False
                    break

            visited.pop()
            # print(node, visited, memo, 'after')
            if node not in memo:
                memo[node] = True
            return memo[node]

        graph = defaultdict(list)
        memo = {}
        for s, t in edges:
            graph[s].append(t)

        dfs(source, [])
        # print(memo)
        return memo[source]