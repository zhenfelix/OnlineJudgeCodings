class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)
        def dfs(i, cur, tot, mul, path):
            if i == n:
                if tot + cur*mul == target:
                    res.append(path)
                    # print(i, cur, tot, mul, path)
                    # print(eval(path))
                return
            x = ord(num[i])-ord('0')
            if cur != 0:
                dfs(i+1, cur*10+x if cur > 0 else cur*10-x, tot, mul, path+num[i])
            dfs(i+1, x, tot+cur*mul, 1, path+"+"+num[i])
            dfs(i+1, -x, tot+cur*mul, 1, path+"-"+num[i])
            dfs(i+1, x, tot, cur*mul, path+"*"+num[i])
            return
        dfs(1, ord(num[0])-ord('0'), 0, 1, num[0])
        # print(len(res))
        return res


# class Solution:
#     def addOperators(self, num: str, target: int) -> List[str]:
#         n = len(num)
#         res =[]
#         if not num:
#             return res
#         def dfs(idx, cur):
#             if idx == n:
#                 # print(cur)
#                 try:
#                     if eval(cur) == target and eval(cur+"*1") == target:
#                         res.append(cur)
#                 except:
#                     pass
#                 return

#             for sym in ['+','-','*']:
#                 dfs(idx+1,cur+sym+num[idx])
#             dfs(idx+1,cur+num[idx])
#             return
#         dfs(1,num[0])
#         return res


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)
        def dfs(i, path, pre):
            if i == n:
                t = eval(path)
                if t == target:
                    res.append(path)
                return
            dfs(i+1, path+"+"+num[i], len(path)+1)
            dfs(i+1, path+"-"+num[i], len(path)+1)
            dfs(i+1, path+"*"+num[i], len(path)+1)
            if path[pre] != "0":
                dfs(i+1, path+num[i], pre)
            return
        dfs(1,num[0],0)
        return res
