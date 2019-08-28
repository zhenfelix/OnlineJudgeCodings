class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visit = {}
        for i, u in enumerate(username):
            if u not in user_visit:
                user_visit[u] = []
            user_visit[u] += [(timestamp[i],website[i])]
        
        tri_seq = {}
        for k, v in user_visit.items():
            user_visit[k] = sorted(v, key=lambda x: x[0])
            n = len(v)
            if n > 2:
                seq = set()
                for i in range(n):
                    for j in range(i+1,n):
                        for p in range(j+1,n):
                            seq.add((user_visit[k][i][1],user_visit[k][j][1],user_visit[k][p][1]))
                for s in seq:
                    if s not in tri_seq:
                        tri_seq[s] = 1
                    else:
                        tri_seq[s] += 1
                        
        # print(tri_seq.items())
        # print(sorted(tri_seq.items(), key=lambda x: (-x[1], x[0][0], x[0][1], x[0][2]))[0])
        ans = sorted(tri_seq.items(), key=lambda x: (-x[1], x[0][0], x[0][1], x[0][2]))[0][0]
        return list(ans)
                            