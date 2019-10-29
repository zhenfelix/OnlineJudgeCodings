# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         def  dfs(idx, path):
#             # print(idx, path)
#             if n-idx > (4-len(path))*3:
#                 return
#             if len(path) == 4:
#                 if idx >= n:
#                     res.append('.'.join(path))
#                 return
#             if idx < n and s[idx] == '0':
#                 dfs(idx+1, path+['0'])
#                 return
#             for i in range(idx+1,min(idx+4,n+1)):
#                 if 0 < int(s[idx:i]) <= 255:
#                     dfs(i, path+[s[idx:i]])
#             return
#         res, n = [], len(s)
#         dfs(0, [])
#         return res

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def  dfs(cur, path):
            # print(cur, path)
            if len(cur) > (4-len(path))*3:
                return
            if len(path) == 4:
                if cur:
                    return
                # print(path)
                res.append('.'.join(path))
                return
            if cur and cur[0] == '0':
                dfs(cur[1:], path+['0'])
                return
            for i in range(1,min(4,len(cur)+1)):
                if 0 < int(cur[:i]) <= 255:
                    dfs(cur[i:], path+[cur[:i]])
            return
        res = []
        dfs(s, [])
        return res