import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():




    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        n, m, r, c = map(int,input().split(' '))
        start = 0
        dp = [[0]*m for _ in range(n)]
        flag = True
        for i in range(n):
            for j in range(start,start+r):
                dp[i][j%m] = 1
                if j//m+1 > c:
                    flag = False
                    break
            start += r
        if start%m or start//m != c: flag = False
        if flag:
            print('YES')
            for i in range(n):
                print(''.join(map(str,dp[i])))
        else:
            print('NO')





if __name__ == "__main__":
    main()




