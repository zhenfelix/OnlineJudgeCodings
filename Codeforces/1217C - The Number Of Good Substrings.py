import sys, heapq
from collections import *
from functools import lru_cache



def main():

    def solve(s):
        n = len(s)
        ans = 0
        last = -1
        for i in range(n):
            if s[i] == '0':
                continue
            cur = 0
            for j in range(i,min(i+20,n)):
                cur <<= 1
                cur |= int(s[j])
                if last <= j-cur < i:
                    ans += 1
            last = i
        return ans 

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    t = int(input())
    for _ in range(t):
        s = input()
        print(solve(s))

    # debug(ans)


if __name__ == "__main__":
    main()


