# class Solution:
#     def dfs(self, graph, path, cur, ans):
#         path.append(cur)
#         if cur==len(graph)-1:
#             ans.append(path.copy())
#         else:
#             for node in graph[cur]:
#                 self.dfs(graph, path, node, ans)
#         path.pop()
#         return
            
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         ans=[]
#         path=[]
#         self.dfs(graph,path,0,ans)
#         return ans

class Solution(object):
    def allPathsSourceTarget(self, graph):
        def dfs(cur, path):
            if cur == len(graph) - 1: res.append(path)
            else:
                for i in graph[cur]: dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res