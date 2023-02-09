# // CF74C
import sys, heapq
from collections import *
from functools import lru_cache
from math import *



def main():

    def solve():
        n, m = map(int, input().split())
        print(gcd(n-1,m-1)+1)
        return 

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    t = 1
    for _ in range(t):
        solve()

    # debug(ans)


if __name__ == "__main__":
    main()


