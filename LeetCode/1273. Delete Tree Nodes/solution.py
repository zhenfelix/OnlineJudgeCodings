# class Solution:
#     def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
#         mp = collections.defaultdict(list)
#         for i, p in enumerate(parent):
#             if p >= 0:
#                 mp[p].append(i)

#         def dfs(cur):
#             cnt = 1
#             for child in mp[cur]:
#                 val, cc = dfs(child)
#                 cnt += cc 
#                 value[cur] += val 
#             if value[cur] == 0:
#                 return 0, 0
#             return value[cur], cnt

#         _, res = dfs(0)
#         return res

# class Solution:
#     def deleteTreeNodes(self, n, parent, value):
#         sons = {i: set() for i in range(n)}
#         for i, p in enumerate(parent):
#             if i: sons[p].add(i)

#         def dfs(x):
#             total, count = value[x], 1
#             for y in sons[x]:
#                 t, c = dfs(y)
#                 total += t
#                 count += c if t else 0
#             return total, count if total else 0
#         return dfs(0)[1]



class Solution:
    def deleteTreeNodes(self, n, parent, value):
        res = [1] * n
        for i in range(n)[::-1]:
            value[parent[i]] += value[i]
            res[parent[i]] += res[i] if value[i] else 0
        return res[0]