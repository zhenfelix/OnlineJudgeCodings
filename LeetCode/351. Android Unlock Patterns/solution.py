from collections import Counter

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def dfs(cur, visited, x):
            if m <= x <= n:
                res[0] += 1
            
            if x == n:
                return
            else:
                for nxt in range(1,10):
                    if nxt not in visited:
                        if not cur:
                            pass
                        elif nxt + cur == 10 and 5 not in visited:
                            continue
                        elif (nxt + cur) & 1 or (5 in [cur, nxt]) or (nxt & 1 and cur & 1 and (cur+nxt)//2 in visited) or (nxt & 1 == 0 and cur & 1 == 0):
                            pass
                        else:
                            continue
                        visited.add(nxt)
                        dfs(nxt, visited, x+1)
                        visited.remove(nxt)
            
        res = [0]
        # visited = set()
        # dfs(None, visited, 0)
        for start in range(1,3):
            visited = set([start])
            dfs(start, visited, 1)
        res[0] = res[0]*4
       
        for start in [5]:
            visited = set([start])
            dfs(start, visited, 1)
        
        
        return res[0]
                            