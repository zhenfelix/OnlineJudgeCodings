class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        todo = []
        def find(cur):
            if cur not in parent:
                parent[cur] = cur
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
            return
            
        for eq in equations:
            u, v = eq[0], eq[-1]
            if eq [1:3] == "!=":
                todo.append((u,v))
            else:
                union(u,v)
        for u, v in todo:
            if find(u) == find(v):
                return False
        return True

