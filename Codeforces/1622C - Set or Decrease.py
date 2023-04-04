from random import *
import sys
from collections import * 
from math import * 
from functools import *
from heapq import *



def solve(n,k,arr):
    arr.sort()
    tot = s = sum(arr)
    # if s <= k: return 0
    ans = max(0,s-k)
    for j in range(1,n)[::-1]: 
        s -= (arr[j]-arr[0])
        ans = min(ans, n-j+max(0,(s-k-1)//(n-j+1)+1))
    return ans 


def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    case = int(input())
    for _ in range(case):
        n, k = list(map(int,input().split()))
        # n = int(input())
        arr = list(map(int,input().split()))
        # brr = list(map(int,input().split()))
        # s = input()
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        print(solve(n,k,arr))
        

if __name__ == "__main__":
    main()