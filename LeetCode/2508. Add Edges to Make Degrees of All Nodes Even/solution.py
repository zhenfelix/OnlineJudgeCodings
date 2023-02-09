class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        cc = Counter()
        for u, v in edges:
            u -= 1
            v -= 1
            seen.add((u,v))
            seen.add((v,u))
            cc[u] += 1
            cc[v] += 1 
        candidates = []
        for i in range(n):
            if cc[i]%2 == 1:
                candidates.append(i)
        # print(candidates)
        if len(candidates) == 0:
            return True
        if len(candidates) == 2:
            u,v = candidates
            if (u,v) not in seen:
                return True 
            for i in range(n):
                if i == u or i == v: continue
                if (i,u) not in seen and (i,v) not in seen:
                    return True
            return False
        if len(candidates) == 4:
            u,v,x,y = candidates
            loops = [(u,v,x,y),(u,x,v,y),(u,y,v,x)]
            for a,b,c,d in loops:
                if (a,b) not in seen and (c,d) not in seen:
                    return True
        return False
