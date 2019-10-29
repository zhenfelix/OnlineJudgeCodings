# class Solution:
#     def circularPermutation(self, n: int, start: int) -> List[int]:
#         def dfs(cur, visited, path):
#             # print(cur, visited, path)
#             if len(path) == (1<<n):
#                 # print(path)
#                 res[0] = path
#                 return True
#             for i in range(n):
#                 if (cur & (1<<i)) > 0:
#                     nxt = cur - (1<<i)
#                 else:
#                     nxt = cur + (1<<i)
#                 if nxt not in visited:
#                     visited.add(nxt)
#                     if dfs(nxt, visited, path+[nxt]):
#                         return True
#                     visited.remove(nxt)
#             return False
#         res = [[]]
#         dfs(start, set([start]), [start])
#         return res[0]

class Solution:
    # def circularPermutation(self, n: int, start: int) -> List[int]:
    #     res = [0,1]
    #     for i in range(1,n):
    #         res += [p+(1<<i) for p in res[::-1]]
    #     idx = res.index(start)
    #     return res[idx:]+res[:idx]
    

      def circularPermutation(self, n, start):
        return [start ^ i ^ (i >> 1) for i in range(1 << n)]