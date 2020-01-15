class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        n = len(s)
        cc = collections.Counter(s)
        mid = ""
        sums = 0
        for k,v in cc.items():
            sums += (v&1)
            if v&1:
                mid = k 
        if sums > 1:
            return []
        
        res = []
        def dfs(cc,path,res):
            if len(path) == n//2:
                res.append(path+mid+path[::-1])
                return
            for k, v in cc.items():
                if v > 1:
                    cc[k] -= 2
                    dfs(cc, path+k, res)
                    cc[k] += 2
            return
        dfs(cc, "", res)
        return res