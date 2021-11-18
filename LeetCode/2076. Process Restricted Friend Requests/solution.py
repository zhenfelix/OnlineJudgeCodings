class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def merge(u, v):
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv
            return

        m = len(requests)
        res = [True]*m 
        for i, (a,b) in enumerate(requests):
            pa, pb = find(a), find(b)
            for u, v in restrictions:
                pu, pv = find(u), find(v)
                if (pu == pa and pv == pb) or  (pu == pb and pv == pa):
                    res[i] = False
                    break
            if res[i]:
                merge(a,b)
        return res


