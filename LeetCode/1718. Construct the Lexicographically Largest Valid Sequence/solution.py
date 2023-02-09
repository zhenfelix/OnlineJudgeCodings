class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = n*2-1
        path = [0]*m
        def dfs(i, path, visited):
            if i == m:
                return True
            if path[i] != 0:
                return dfs(i+1, path, visited)
            for v in range(1,n+1)[::-1]:
                if visited[v]: continue 
                if v > 1 and (i+v >= m or path[i+v] != 0): continue
                path[i] = v 
                if v > 1: path[i+v] = v 
                visited[v] = 1
                if dfs(i+1, path, visited):
                    return True 
                visited[v] = 0
                if v > 1: path[i+v] = 0
                path[i] = 0
            return False
        dfs(0,path,[0]*(n+1))
        return path

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

