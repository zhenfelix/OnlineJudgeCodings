class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = defaultdict(list)
        for i, p in enumerate(parent):
            if p >= 0:
                g[p].append(i)
        ans = 0
        cc = Counter()
        def dfs(cur, v):
            nonlocal ans 
            # old = ans
            ans += cc[v]
            for i in range(26):
                ans += cc[v^(1<<i)]
            # print(cur,ans-old,cc)
            cc[v] += 1
            for nxt in g[cur]:
                ch = ord(s[nxt])-ord('a')
                dfs(nxt,v^(1<<ch))
            return 
        dfs(0,0)
        return ans
