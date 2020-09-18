class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(x,pp):
            if x != pp[x]:
                pp[x] = find(pp[x],pp)
            return pp[x]


        def union(x,y,pp):
            rx, ry = find(x,pp), find(y,pp)
            if rx == ry:
                return 1
            pp[rx] = ry
            return 0

        mp = defaultdict(list)
        for t, a, b in edges:
            a -= 1
            b -= 1
            mp[t].append((a,b))
        parent = [i for i in range(n)]
        res = 0
        for a, b in mp[3]:
            res += union(a,b,parent)
        parent1 = parent.copy()
        for a, b in mp[1]:
            res += union(a,b,parent1)
        if len(set([find(i,parent1) for i in range(n)])) != 1:
            return -1
        parent2 = parent.copy()
        for a, b in mp[2]:
            res += union(a,b,parent2)
        if len(set([find(i,parent2) for i in range(n)])) != 1:
            return -1
        return res 
