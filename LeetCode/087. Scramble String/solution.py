# from collections import Counter
from functools import lru_cache
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        @lru_cache(None)
        def dfs(i,j,k):
            # print(i,j,k)
            if k == 1:
                return s1[i] == s2[j]
            # if s1[i:i+k] == s2[j:j+k]:
            #     return True
            for d in range(1, k):
                if (dfs(i,j,d) and dfs(i+d,j+d,k-d)) or (dfs(i,j+k-d,d) and dfs(i+d,j,k-d)):
                    return True
            return False
        return dfs(0,0,len(s1))

