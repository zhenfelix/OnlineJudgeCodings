import functools


class Solution:
    def kmp(self, s):
        m = len(s)
        nxt = [-1] * (m + 1)
        i, j = 0, -1
        while i < m:
            if j == -1 or s[i] == s[j]:
                i += 1
                j += 1
                nxt[i] = j
            else:
                j = nxt[j]
        return nxt

    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        nxt = self.kmp(evil)
        # print(nxt)
        M = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(cur, f1, f2, state):
            if state == len(evil):
                return 0
            if cur == n:
                return 1
            lo, hi = ord('a'), ord('z')
            if f1:
                lo = ord(s1[cur])
            if f2:
                hi = ord(s2[cur])
            cnt = 0
            for ch in range(lo, hi + 1):
                ch = chr(ch)
                j = state
                while j != -1 and ch != evil[j]:
                    j = nxt[j]
                j += 1
                cnt += dfs(cur + 1, f1 and ch == s1[cur], f2 and ch == s2[cur], j)
            return cnt % M

        return dfs(0, True, True, 0)