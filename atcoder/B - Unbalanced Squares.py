import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():

    # def solve(n):
    #     mat = [[0]*n for _ in range(n)]
    #     visited = [[0]*n for _ in range(n)]
    #     i, j, cnt = 0, 0, 0
    #     cur = n
    #     def check(r,c):
    #         return 0 <= r < n and 0 <= c < n 
    #     while cnt < n*n:
    #         rank = 0
    #         lo, hi = cnt+1, cnt+cur**2-(max(0,cur-2))**2
    #         cur -= 2
    #         while cnt < n*n and check(i,j) and mat[i][j] == 0:
    #             if rank&1:
    #                 mat[i][j] = lo 
    #                 lo += 1
    #             else:
    #                 mat[i][j] = hi 
    #                 hi -= 1
    #             j += 1
    #             rank += 1
    #             cnt += 1
    #         j -= 1
    #         i += 1
    #         while cnt < n*n and check(i,j) and mat[i][j] == 0:
    #             if rank&1:
    #                 mat[i][j] = lo 
    #                 lo += 1
    #             else:
    #                 mat[i][j] = hi 
    #                 hi -= 1
    #             i += 1
    #             rank += 1
    #             cnt += 1
    #         i -= 1
    #         j -= 1
    #         while cnt < n*n and check(i,j) and mat[i][j] == 0:
    #             if rank&1:
    #                 mat[i][j] = lo 
    #                 lo += 1
    #             else:
    #                 mat[i][j] = hi 
    #                 hi -= 1
    #             rank += 1
    #             cnt += 1
    #             j -= 1
    #         j += 1
    #         i -= 1
    #         while cnt < n*n and check(i,j) and mat[i][j] == 0:
    #             if rank&1:
    #                 mat[i][j] = lo 
    #                 lo += 1
    #             else:
    #                 mat[i][j] = hi 
    #                 hi -= 1
    #             rank += 1
    #             cnt += 1
    #             i -= 1
    #         i += 1
    #         j += 1
    #     return mat

    def solve(n):
        mat = [[0]*n for _ in range(n)]
        lo, hi = 1, n*n 
        for i in range(n):
            for j in range(n):
                if (i+j)&1:
                    mat[i][j] = lo 
                    lo += 1
                else:
                    mat[i][j] = hi 
                    hi -= 1
        return mat

    def debug(mat):
        print("\n\n---debug----\n\n")
        n = len(mat)
        for i in range(1,n-1):
            for j in range(1,n-1):
                lo, hi = 0, 0
                for di in range(i-1,i+2):
                    for dj in range(j-1,j+2):
                        if (di,dj) == (i,j):
                            continue
                        if mat[di][dj] < mat[i][j]:
                            lo += 1
                        else:
                            hi += 1
                if lo == hi:
                    print(mat[i][j],(i,j,lo,hi))
        return



    # sys.stdin = open('input.txt', 'r')
    # print(input().split(' '))
    n = int(input())
    ans = solve(n)
    for a in ans:
        print(*a)

    # debug(ans)


if __name__ == "__main__":
    main()


