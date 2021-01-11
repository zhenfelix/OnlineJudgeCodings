class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [-1]*(2*n-1)
        visited = set()
        def dfs(idx):
            if idx == 2*n-1:
                return True
            if res[idx] != -1:
                return dfs(idx+1)
            for i in range(1,n+1)[::-1]:
                if i in visited or (i > 1 and idx+i >= 2*n-1) or (i > 1 and res[idx+i] != -1):
                    continue 
                visited.add(i)
                res[idx] = i 
                if i > 1:
                    res[idx+i] = i 
                # print(res,idx,i)
                if dfs(idx+1):
                    return True
                visited.remove(i)
                res[idx] = -1
                if i > 1:
                    res[idx+i] = -1                            
            return False
        # print(dfs(0))
        dfs(0)
        return res 

