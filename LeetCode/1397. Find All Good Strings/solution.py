from random import *
import sys
from collections import * 
from math import * 
from functools import *
from heapq import *
from string import *

ascii_lowercase = "ab"

def kmp(pattern):
    sz = len(pattern)
    fail = [-1]*(sz+1)
    j = -1 
    for i in range(sz):
        ch = pattern[i]
        while j != -1 and pattern[j] != ch:
            j = fail[j]
        j += 1 
        fail[i+1] = j 
    return fail

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9+7
        mp = {ch: i for i, ch in enumerate(ascii_lowercase)}
        f = lambda x: mp[x]
        s1 = list(map(f,s1))
        s2 = list(map(f,s2))
        evil = list(map(f,evil))
        fail = kmp(evil)
        fmp = [[-1]*(len(evil)+1) for _ in range(len(ascii_lowercase))]
        m = len(evil)
        for ch in range(len(ascii_lowercase)):
            for j in range(m):
                t = j
                while t < len(evil) and t != -1 and evil[t] != ch:
                    t = fail[t]
                t += 1
                fmp[ch][j] = t
            fmp[ch][m] = m 

        a, z = ord(ascii_lowercase[0])-ord(ascii_lowercase[0]), ord(ascii_lowercase[-1])-ord(ascii_lowercase[0])

        @lru_cache(None)
        def dfs(i,j,flo,fhi):
            if i == n: return j != len(evil) 
            hi = s2[i] if fhi else z
            lo = s1[i] if flo else a
            res = 0
            for ch in range(lo,hi+1):
                res += dfs(i+1,fmp[ch][j],flo and ch == lo, fhi and ch == hi)
            return res%MOD  
        return dfs(0,0,True,True)

        # tot = (m+1)*4
        # dp = [1]*tot
        # for i in range(4): dp[i*(m+1)+m] = 0
        # for i in range(n)[::-1]:
        #     ndp = [0]*tot 
        #     for cur in range(4):
        #         hi = s2[i] if cur&1 else z
        #         lo = s1[i] if cur&2 else a
        #         for j in range(m+1):
        #             for ch in range(lo,hi+1):
        #                 nxt = cur
        #                 tmp = 0
        #                 if ch == lo: tmp |= 2
        #                 if ch == hi: tmp |= 1
        #                 nxt &= tmp
        #                 ndp[cur*(m+1)+j] += dp[nxt*(m+1)+fmp[ch
        #         ][j]]
        #             ndp[cur*(m+1)+j] %= MOD 
        #     dp = ndp 
        # return dp[3*(m+1)]
    
def genseq(n,i,path,s,e,flo,fhi):
    if i == n: 
        yield path
        return
    lo = s[i] if flo else ascii_lowercase[0]
    hi = e[i] if fhi else ascii_lowercase[-1]
    for ch in ascii_lowercase:
        if lo <= ch <= hi:
            yield from genseq(n,i+1,path+ch,s,e,flo and ch == lo, fhi and ch == hi)
    return



def brute(n,s1,s2,evil):
    g = genseq(n,0,'',s1,s2,True,True)
    cnt = 0
    for s in g:
        if evil in s: 
            # print(s)
            continue
        cnt += 1
    return cnt 

def generate():
    
    n = randint(1,10)
    m = randint(1,n)
    s1 = ''.join(choices(ascii_lowercase,k=n))
    s2 = ''.join(choices(ascii_lowercase,k=n))
    if s1 > s2: s1, s2 = s2, s1 
    evil = ''.join(choices(ascii_lowercase,k=m))
    return n,s1,s2,evil




def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    # case = int(input())
    for i in range(100):
        # n, k = list(map(int,input().split()))
        # brr = list(map(int,input().split()))
        # s = input()
        n,s1,s2,evil = generate()
        # n,s1,s2,evil = 4,'aaab','baba','aa'
        sol = Solution()
        ans1 = sol.findGoodStrings(n,s1,s2,evil)
        ans2 = brute(n,s1,s2,evil)

        assert(ans1 == ans2)
        print(f"{i}th test case ok")
        

if __name__ == "__main__":
    main()


# import functools
# class Solution:
#     def kmp(self, s):
#         m = len(s)
#         nxt = [-1] * (m + 1)
#         i, j = 0, -1
#         while i < m:
#             if j == -1 or s[i] == s[j]:
#                 i += 1
#                 j += 1
#                 nxt[i] = j
#             else:
#                 j = nxt[j]
#         return nxt

#     def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
#         nxt = self.kmp(evil)
#         # print(nxt)
#         M = 10 ** 9 + 7

#         @functools.lru_cache(None)
#         def dfs(cur, f1, f2, state):
#             if state == len(evil):
#                 return 0
#             if cur == n:
#                 return 1
#             lo, hi = ord('a'), ord('z')
#             if f1:
#                 lo = ord(s1[cur])
#             if f2:
#                 hi = ord(s2[cur])
#             cnt = 0
#             for ch in range(lo, hi + 1):
#                 ch = chr(ch)
#                 j = state
#                 while j != -1 and ch != evil[j]:
#                     j = nxt[j]
#                 j += 1
#                 cnt += dfs(cur + 1, f1 and ch == s1[cur], f2 and ch == s2[cur], j)
#             return cnt % M

#         return dfs(0, True, True, 0)