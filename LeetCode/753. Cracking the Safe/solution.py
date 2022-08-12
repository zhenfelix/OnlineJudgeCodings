class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        g = defaultdict(int)
        path = []
        def dfs(cur, pch):
            while g[cur] < k:
                ch = str(g[cur])
                g[cur] += 1
                dfs((cur+ch)[1:], ch)
            path.append(pch)
        dfs('0'*(n-1), '0'*(n-1))
        return ''.join(path)



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
        # dfs('0' * (n-1), k, set(), ans)
        start = ''.join(list(map(lambda x: str(x%k), range(n-1))))
        dfs(start, k, set(), ans)
        return ''.join(ans) + start[::-1]

    def crackSafe(self, n: int, k: int) -> str:

        st = []
        visited = set()
        ans = []
        st.append('0'*n)
        while st:
            # print(st)
            cur = st[-1][1:]
            flag = True
            for x in map(str, range(k)):
                edge = cur + x
                if edge not in visited:
                    visited.add(edge)
                    st.append(edge)
                    flag = False
                    break
            if flag:
                ans.append(st.pop()[-1])
            # print(ans)
        return ''.join(ans[:-1]) + '0'*(n-1)
            
        


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
                