class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        n = len(word)
        def dfs(idx, path):
            if idx == n:
                res.append(path)
                # print(path)
                return
            dfs(idx+1,path+word[idx])
            if path and path[-1] != word[idx-1]:
                return
            for nxt in range(idx,n):
                dfs(nxt+1,path+str(nxt-idx+1))
            return
        dfs(0,"")
        return res