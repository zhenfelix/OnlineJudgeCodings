class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        mp = {r: i for i, r in enumerate(recipes)}
        res = []
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for i, ingredient in enumerate(ingredients):
            indegree[recipes[i]] = len(ingredient)
            for r in ingredient:
                graph[r].append(recipes[i])
        
        # print(indegree)

        q = deque(supplies)
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    res.append(nxt)
                    q.append(nxt)
        # print(indegree)
        return res

