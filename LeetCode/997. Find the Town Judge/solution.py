# class Solution:
#     def findJudge(self, N: int, trust: List[List[int]]) -> int:
#         cc = {}
#         mp = set()
#         for i in range(1,N+1,1):
#             cc[i] = 0
#         for t in trust:
#             cc[t[1]] += 1
#             if t[0] not in mp:
#                 mp.add(t[0])
        
#         for k, v in cc.items():
#             if v == N-1 and k not in mp:
#                 return k
#         return -1

class Solution:
    def findJudge(self, N, trust):
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1
        
            