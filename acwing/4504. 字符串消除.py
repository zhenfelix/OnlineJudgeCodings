import sys, heapq
from collections import *
from functools import lru_cache



def main():

    def solve(s):
        st = []
        cnt = 0
        for ch in s:
            if st and st[-1] == ch:
                st.pop()
                cnt += 1
            else:
                st.append(ch)
        if cnt&1:
            print("Yes")
        else:
            print("No")
        return 

    # sys.stdin = open('contests/input', 'r')
    # print(input().split(' '))
    s = input()
    t = 1
    for _ in range(t):
        solve(s)

    # debug(ans)


if __name__ == "__main__":
    main()


