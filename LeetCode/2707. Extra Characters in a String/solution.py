class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary = set(dictionary)
        seen = set()
        for i in range(n):
            for j in range(i+1,n+1):
                if s[i:j] in dictionary:
                    seen.add((i,j))

        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 0
            res = n-i
            for j in range(i+1,n+1):
                res = min(res, dfs(j)+(0 if (i,j) in seen else j-i))
            return res
        return dfs(0)