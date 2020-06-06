import sys, heapq
from collections import *
from functools import lru_cache
sys.setrecursionlimit(10**6)



def main():

    def dfs(idx,path,diff):
        nonlocal res
        if idx == m:
            res = path
            return True
        s0, s1 = set(), set()
        for i in range(n):
            if diff & (1<<i):
                s1.add(arr[i][idx])
            else:
                s0.add(arr[i][idx])
        if len(s1) > 1:
            return False
        for ch in (s0|s1):
            newdiff = diff
            for i in range(n):
                if newdiff&(1<<i) and arr[i][idx]!=ch:
                    break
                if arr[i][idx]!=ch:
                    newdiff = newdiff|(1<<i)
            else:
                if dfs(idx+1,path+ch,newdiff):
                    return True
        return False


    # sys.stdin = open('input.txt', 'r')
    t = int(input())
    for _ in range(t):
        n, m = map(int,input().split(' '))
        arr = []
        res = ''
        for i in range(n):
            s = input()
            arr.append(s)
        if dfs(0,'',0):
            print(res)
        else:
            print(-1)





if __name__ == "__main__":
    main()




