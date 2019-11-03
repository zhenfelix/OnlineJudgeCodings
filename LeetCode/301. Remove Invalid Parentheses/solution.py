# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         def dfs(idx, path, left, cnt):
#             # print(idx,path,st,cnt)
#             if left > n-len(path) or cnt > n-len(path):
#                 return
            
#             if idx == n:
#                 if left == 0:
#                     res[0].add(path)
#                 return
#             if s[idx] not in "()":
#                 dfs(idx+1,path+s[idx],left,cnt)
#                 return
#             if cnt > 0:
#                 dfs(idx+1,path,left,cnt-1)
#             if s[idx] == ')':
#                 if left > 0:
#                     dfs(idx+1,path+s[idx],left-1,cnt)
#             else:
#                 dfs(idx+1,path+s[idx],left+1,cnt)
#             return


#         res = [set()]
#         n = len(s)
#         for i in range(n+1):
#             dfs(0,"",0,i)
#             if res[0]:
#                 break
#         return res[0]



class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l, r = 0, 0
        for ch in s:
            if ch not in "()":
                continue
            if ch == '(':
                l += 1
            elif l > 0:
                l -= 1
            else:
                r += 1

        def dfs(idx, path, left, right, cnt):
            # print(idx,path,st,cnt)
            if left+right > n-len(path) or cnt < 0 or left < 0 or right < 0:
                return
            
            if idx == n:
                if cnt == 0:
                    res[0].add(path)
                return
            if s[idx] not in "()":
                dfs(idx+1,path+s[idx],left,right,cnt)
                return
            if s[idx] == '(':
                dfs(idx+1,path,left-1,right,cnt)
                dfs(idx+1,path+s[idx],left,right,cnt+1)
            else:
                dfs(idx+1,path,left,right-1,cnt)
                dfs(idx+1,path+s[idx],left,right,cnt-1)

            return


        res = [set()]
        n = len(s)
        dfs(0,"",l,r,0)
        return res[0]

