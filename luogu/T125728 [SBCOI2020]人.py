# https://www.luogu.com.cn/problem/T125728?contestId=27163
# https://www.luogu.com.cn/blog/12cow/SBCOI2020

# import sys, heapq
# from collections import *
# from functools import lru_cache
# sys.setrecursionlimit(10**6)


# @lru_cache(None)
# def em(mm, aa, bb):
#     if mm == aa+bb: res = 0
#     elif aa+bb == 0: return 1
#     else: res = (em(mm-1,aa,bb)+od(mm-1,aa,bb)+ev(mm-1,aa,bb))%Mod
#     # print(0, mm,aa,bb,res)
#     return res

# @lru_cache(None)
# def od(mm, aa, bb):
#     if aa == 0: res = 0
#     elif mm == aa+bb: res = 1 if bb == 0 else 0
#     else: res = (em(mm-1,aa-1,bb)+od(mm-1,aa-1,bb))%Mod
#     # print(1, mm, aa, bb, res)
#     return res

# @lru_cache(None)
# def ev(mm, aa, bb):
#     if bb == 0: res = 0
#     elif mm == aa+bb: res = 1
#     else: res = (em(mm-1,aa,bb-1)+od(mm-1,aa,bb-1)+ev(mm-1,aa,bb-1))%Mod
#     # print(2, mm, aa, bb, res)
#     return res



# # sys.stdin = open('input.txt', 'r')
# t = input()
# t = int(t)
# Mod = 998244353
# for _ in range(t):
#     m, a, b = map(int, input().split(' '))
#     print((em(m,a,b)+od(m,a,b)+ev(m,a,b))%Mod)


import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**8)



def main():
    @lru_cache(None)
    def dfs(mm, aa, bb):
        # print(mm,aa,bb)
        if mm == aa + bb:
            res = 1
        elif aa + bb == 0:
            res = 1
        elif aa == 0:
            res = (dfs(mm - 1, 0, bb) + dfs(mm - 1, 0, bb - 1)) % Mod
        elif bb == 0:
            res = (dfs(mm - 1, aa, 0) + dfs(mm - 1, aa - 1, 0)) % Mod
        else:
            res = (dfs(mm - 1, aa, bb) + dfs(mm - 1, aa, bb - 1) + dfs(mm - 1, aa - 1, bb) - dfs(mm - 2, aa - 1,
                                                                                                 bb - 1)) % Mod
        # print('**', mm,aa,bb,res)
        return res

    sys.stdin = open('input.txt', 'r')
    t = int(input())
    dfs(100,100,100)
    Mod = 998244353
    for _ in range(t):
        m, a, b = map(int, input().split(' '))
        print(dfs(m, a, b))


if __name__ == "__main__":
    main()


