class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i,r,path):
            if r == 0:
                res.append(path)
                return
            for j in range(i,n-r+2):
                dfs(j+1,r-1,path+[j])
            return
        dfs(1,k,[])
        return res