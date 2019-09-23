# class Solution:
#     def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
#         n = len(s)
#         parent = [i for i in range(n)]
        
#         def find(x):
#             if parent[x] != x:
#                 parent[x] = find(parent[x])
#             return parent[x]
                
#         def union(x, y):
#             parent[find(x)] = find(y)
        
#         for pair in pairs:
#             union(pair[0], pair[1])
            
#         mat = []
#         mp = {}
#         for i in range(n):
#             if find(i) not in mp:
#                 mp[find(i)] = len(mat)
#                 mat.append([])
#             mat[mp[find(i)]].append(i)
            
#         for idx, row in enumerate(mat):
#             mat[idx] = sorted(row, key = lambda x: s[x])[::-1]
        
#         res = ""
#         for i in range(n):
#             res += s[mat[mp[find(i)]].pop()]
        
#         return res


from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
           class UF:
               def __init__(self, n): self.p = list(range(n))
               def union(self, x, y): self.p[self.find(x)] = self.find(y)
               def find(self, x):
                   if x != self.p[x]: self.p[x] = self.find(self.p[x])
                   return self.p[x]
           uf, res, m = UF(len(s)), [], defaultdict(list)
           for x,y in pairs: 
               uf.union(x,y)
           for i in range(len(s)): 
               m[uf.find(i)].append(s[i])
           for comp_id in m.keys(): 
               m[comp_id].sort(reverse=True)
           for i in range(len(s)): 
               res.append(m[uf.find(i)].pop())
           return ''.join(res)
            