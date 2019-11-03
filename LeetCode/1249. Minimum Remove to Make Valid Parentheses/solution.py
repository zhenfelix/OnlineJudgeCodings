class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l, r = 0, 0
        res = ""
        for ch in s:
            if ch not in "()":
                res += ch
                continue
            if ch == '(':
                res += ch
                l += 1
            elif l > 0:
                res += ch
                l -= 1
            else:
                r += 1
        tmp = ""
        for ch in res[::-1]:
            if l > 0 and ch == '(':
                l -= 1
            else:
                tmp += ch
        res = tmp[::-1]

        # def dfs(idx, path, left, right, cnt):
        #     # print(idx,path,st,cnt)
        #     if left+right > n-len(path) or cnt < 0 or left < 0 or right < 0:
        #         return False
            
        #     if idx == n:
        #         if cnt == 0:
        #             res[0] = path
        #         return True
        #     if s[idx] not in "()":
        #         if dfs(idx+1,path+s[idx],left,right,cnt):
        #             return True
        #     if s[idx] == '(':
        #         if dfs(idx+1,path,left-1,right,cnt) or dfs(idx+1,path+s[idx],left,right,cnt+1):
        #             return True
                
        #     else:
        #         if dfs(idx+1,path,left,right-1,cnt) or dfs(idx+1,path+s[idx],left,right,cnt-1):
        #             return True

        #     return False


        # res = [""]
        # n = len(s)
        # dfs(0,"",l,r,0)
        return res