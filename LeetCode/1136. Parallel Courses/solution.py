from collections import deque

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        depend = [[] for _ in range(N+1)]
        income = [0] * (N+1)
        # print(depend)
        for re in relations:
            income[re[0]] += 1
            
            depend[re[1]] += [re[0]]
            
         
        q = deque()
        for i in range(1,N+1,1):
            if income[i] == 0:
                q.append(i)
        
        cc, level = 0, 0
        while len(q) > 0:
            n = len(q)
            cc += n
            for _ in range(n):
                front = q.popleft()
                for dpd in depend[front]:
                    income[dpd] -= 1
                    if income[dpd] == 0:
                        q.append(dpd)
            level += 1
        if cc != N:
            return -1
        return level