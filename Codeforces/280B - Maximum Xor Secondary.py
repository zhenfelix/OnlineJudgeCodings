import sys, heapq
from collections import *
from math import inf
from functools import lru_cache
# sys.setrecursionlimit(10**6)



def main():

    def solve(arr):
        st = [inf]
        arr.append(inf)
        ans = 0
        for x in arr:
            while st[-1] < x:
                cur = st.pop()
                if st[-1] != inf:
                    ans = max(ans, cur^st[-1])
                if x != inf:
                    ans = max(ans, cur^x)
            st.append(x)
        return ans 


    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))

    # debug(ans)


if __name__ == "__main__":
    main()


