class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        cc = defaultdict(set)
        records = sorted([(u,t,w) for t,u,w in zip(timestamp,username,website)])
        n = len(records)
        for i in range(n):
            for j in range(i+1,n):
                if records[j][0] != records[i][0]:
                    break
                for k in range(j+1,n):
                    if records[k][0] != records[j][0]:
                        break
                    cc[records[i][-1],records[j][-1],records[k][-1]].add(records[i][0])
        ans, cnt = [], 0
        for k, v in cc.items():
            if len(v) > cnt or (len(v) == cnt and k < ans):
                ans = k
                cnt = len(v)
        return list(ans)






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
                            

