import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():
    @lru_cache(None)
    def dfs(idx,remains):
        if idx == b:
            return True
        for i in range(10):
            if idx == 0 and i == 0 : continue

            if ((remains*10+i)%a==0)==(s[idx]=='1'):
                st.append(i)
                if dfs(idx+1,(remains*10+i)%a):
                    return True
                st.pop()
        return False



    # sys.stdin = open('input.txt', 'r')
    a, b = map(int, input().split(' '))
    s = input()
    # print(a,b,s)
    st = []
    if a == 10 and s[0] == '1':
        print(-1)
    else:
        dfs(0,0)
        print(''.join(map(str,st)))
    return


if __name__ == "__main__":
    main()




