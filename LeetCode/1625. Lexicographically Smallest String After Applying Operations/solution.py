class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        res = [s] 
        
        n = len(s)
        visited = set()
        def dfs(cur):
            # print(cur)
            if cur in visited:
                return
            visited.add(cur)
            if cur < res[0]:
                res[0] = cur
            start = (-b)%n
            dfs(cur[start:]+cur[:start])
            tmp = list(map(int,cur))
            for i in range(n):
                if i&1:
                    tmp[i] += a
                    tmp[i] %= 10
            dfs(''.join([str(x) for x in tmp]))
            return
        dfs(s)
        return res[0]

