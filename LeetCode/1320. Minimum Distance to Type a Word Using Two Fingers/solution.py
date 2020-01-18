from functools import lru_cache
class Solution:
    def minimumDistance(self, word: str) -> int:
        word = list(map(lambda x: ord(x)-ord('A'),word))
        n = len(word)
        def dist(a,b):
            return abs(a//6-b//6)+abs(a%6-b%6)
        @lru_cache(None)
        def dfs(x,y,idx):
            if idx == n:
                return 0
            ch = word[idx]
            return min(dfs(ch,y,idx+1)+dist(ch,x),dfs(x,ch,idx+1)+dist(ch,y))
        return min(dfs(i,j,0) for i in range(26) for j in range(26))


class Solution:
    def minimumDistance(self, A):
        def d(a, b):
            return a and abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        dp, dp2 = {(0, 0): 0}, {}
        for c in (ord(c) + 1 for c in A):
            for a, b in dp:
                dp2[c, b] = min(dp2.get((c, b), 3000), dp[a, b] + d(a, c))
                dp2[a, c] = min(dp2.get((a, c), 3000), dp[a, b] + d(b, c))
            dp, dp2 = dp2, {}
        return min(dp.values())



from functools import lru_cache
from sys import setrecursionlimit as srl
srl(10**6)

class Solution(object):
    def minimumDistance(self, word):
        A = [list("ABCDEF"), list("GHIJKL"), list("MNOPQR"), list("STUVWX"), list("YZ    ")]
        R, C = len(A), len(A[0])
        
        index = {}
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                index[val] = r, c
        
        def dist(v1, v2):
            if v1 is None or v2 is None:
                return 0
        
            r1,c1 = index[v1]
            r2,c2 = index[v2]
            return abs(r1-r2) + abs(c1-c2)
        
        @lru_cache(None)
        def dp(i, v1=None, v2=None):
            if i == len(word):
                return 0
            
            # move v1 to i
            ans1 = dist(v1, word[i]) + dp(i+1, word[i], v2)
            ans2 = dist(v2, word[i]) + dp(i+1, v1, word[i])
            return min(ans1, ans2)
        return dp(0)


class Solution:
    def minimumDistance(self, A):
        def d(a, b):
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
        A = [ord(c) - 65 for c in A]
        dp = [0] * 26
        for b, c in zip(A, A[1:]):
            dp[b] = max(dp[a] + d(b, c) - d(a, c) for a in range(26))
        return sum(d(b, c) for b, c in zip(A, A[1:])) - max(dp)