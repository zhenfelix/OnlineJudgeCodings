class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(node, k, visited, ans):
            for x in map(str, range(k)):
                edge = node + x
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:], k, visited, ans)
                    ans.append(x)
                    
        ans = []
        dfs('0' * (n-1), k, set(), ans)
        return ''.join(ans) + '0' * (n-1)



            
        


# class Solution(object):
#     def crackSafe(self, n, k):
#         target = k**n
#         start = '0'*n
        
#         visited = set()
#         visited.add(start)
#         path = ['0']*n
        
#         def dfs(node):
#             if len(visited) == target:
#                 return True
#             cur = node[1:]
#             for ch in list(map(str,range(k))):
#                 if cur+ch not in visited:
#                     visited.add(cur+ch)
#                     path.append(ch)
#                     if dfs(cur+ch):
#                         return True
#                     visited.remove(cur+ch)
#                     path.pop()
#             return False
        
#         dfs(start)
#         # print(path)
#         return "".join(path)
                