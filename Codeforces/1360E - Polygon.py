import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():


    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = []
        for i in range(n):
            s = input()
            dp.append(s)
        flag = True
        for i in range(n-1)[::-1]:
            for j in range(n-1)[::-1]:
                if dp[i][j]=='1' and dp[i+1][j]=='0' and dp[i][j+1]=='0':
                    flag = False
                    break
        if flag:
            print('YES')
        else:
            print('NO')
        # a, b = map(int, input().split(' '))




if __name__ == "__main__":
    main()




