import sys, heapq
from collections import *
from functools import lru_cache



def main():

    def solve(arr):
        n = len(arr)
        cnt = [0]*21
        for i in range(21):
            for j in range(n):
                cnt[i] += (arr[j]>>i)&1
        ans = 0
        for j in range(n):
            x = 0
            for i in range(21):
                if cnt[i]:
                    x |= (1<<i)
                    cnt[i] -= 1
            if x == 0:
                break
            ans += x*x 
        # print(ans)
        return ans 

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    # t = int(input())
    t = 1
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print(solve(arr))

    # debug(ans)


if __name__ == "__main__":
    main()


