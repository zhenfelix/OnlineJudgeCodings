class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left,right,st):
            if left > n:
                return
            if right == n:
                res.append(''.join(st))
                return
            dfs(left+1,right,st+['('])
            if left > right:
                dfs(left,right+1,st+[')'])
            return
        dfs(0,0,[])
        return res 
