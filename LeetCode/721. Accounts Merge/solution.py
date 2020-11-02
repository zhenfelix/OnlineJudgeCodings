class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = defaultdict(list)
        mp = {}
        n = len(accounts)
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
            return
        for i, v in enumerate(accounts):
            name, mails = v[0], v[1:]
            for m in mails:
                idx = mp.get(m,i)
                union(i,idx)
                mp[m] = i 
        for k, v in mp.items():
            res[find(v)].append(k)
        return [[accounts[k][0]]+sorted(v) for k, v in res.items()]

            