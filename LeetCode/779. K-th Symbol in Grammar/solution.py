class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        f = [1]
        for i in range(30):
            f.append(f[-1]*2)
        n -= 1
        k -= 1
        def dfs(nn,kk):
            if nn > 1 and kk > 0:
                if kk%2:
                    return 1-dfs(nn-1,kk//2)
                else:
                    return dfs(nn-1,kk//2)
            return kk
        return dfs(n,k) 