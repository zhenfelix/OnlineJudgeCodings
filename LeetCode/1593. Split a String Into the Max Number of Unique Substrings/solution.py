class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        ans = 0
        def dfs(i, path, word):
            nonlocal ans
            if i == n:
                if word not in path:
                    ans = max(ans, len(path)+(word != ''))
                return
            word += s[i]
            if word not in path:
                path.add(word)
                dfs(i+1, path, '')
                path.remove(word)
            dfs(i+1, path, word)
            return 
        dfs(0,set(),'')
        return ans 



class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        res = [0]
        
        def dfs(idx, path):
            if idx == n:
                if len(set(path)) == len(path):
                    res[0] = max(res[0], len(path))
                return
            if path:
                dfs(idx+1, path[:-1]+[path[-1]+s[idx]])
            dfs(idx+1, path+[s[idx]])
            return

        
        dfs(0, [])
        return res[0]