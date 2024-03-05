class Solution:
    def minimumSeconds(self, land: List[List[str]]) -> int:
        n, m = len(land), len(land[0])
        path = set()
        q = []
        for i in range(n):
            for j in range(m):
                if land[i][j] == '*':
                    q.append((i,j))
                elif land[i][j] == 'S':
                    path.add((i,j))
                    land[i][j] = '*'
        q.append(path.pop())
        path.add(q[-1])
        dist = 0
        dij = [-1,0,1,0,-1]
        while q:
            dist += 1
            nq = []
            for i,j in q:
                for di, dj in zip(dij[1:],dij[:-1]):
                    di += i 
                    dj += j  
                    if 0 <= di < n and 0 <= dj < m and land[di][dj] not in ['*','X']:
                        if (i,j) in path:
                            if land[di][dj] == 'D':
                                return dist 
                            path.add((di,dj))
                        else:
                            if land[di][dj] == 'D':
                                continue
                        land[di][dj] = '*'
                        nq.append((di,dj))
            q = nq 
            
        return -1  