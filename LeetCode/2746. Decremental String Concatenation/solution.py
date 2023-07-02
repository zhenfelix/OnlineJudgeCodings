class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        @lru_cache(None)
        def dfs(a,b,i):
            if i == n:
                return 0
            ans = 0
            ans = max(ans, dfs(a,words[i][-1],i+1)+(b==words[i][0]))
            ans = max(ans, dfs(words[i][0],b,i+1)+(a==words[i][-1]))
            return ans 
        return sum(len(w) for w in words)-dfs(words[0][0],words[0][-1],1)

