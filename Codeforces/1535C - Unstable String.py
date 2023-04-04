from random import *
import sys
from collections import * 
from math import * 
from functools import *



def solve(s):
    n = len(s)
    p1 = p2 = -1
    ans = 0
    for i in range(n):
        if s[i] in '01':
            ch = int(s[i])
            if (i&1) == (ch&1):
                p1 = i
            else:
                p2 = i 
        ans += i-min(p1,p2) 
    return ans 

def main():
    # sys.stdin = open('contests/input', 'r')
    # s = input()
    case = int(input())
    for _ in range(case):
        # n, m = list(map(int,input().split()))
        # n = int(input())
        # arr = list(map(int,input().split()))
        # brr = list(map(int,input().split()))
        s = input()
        # prizes = list(map(int,input().split()))
        # persons = list(map(int,input().split()))
        # n = randint(1,1000)
        print(solve(s))
        # ans = solve(s)
        # print(f'{round(ans,3):.3f}')
        # print(f'{0.0:.3f}')
        # m = verify(s)
        # assert(m == n)
        # print(n,s,'ok')
        # print(get_num_without_prize(persons, prizes))
        # print(solve(n,m,vs,ws,cnts))
        # if solve(n,l,r):
        #     print("Yes")
        # else:
        #     print("No")
    # a, b = list(map(int,input().split()))

    # for i in range(1000):
    #     b = randint(1,10000000)
    #     a = randint(1,b)
    #     assert(solve(a,b) == solve_another(a,b))
    #     print(i,a,b,'ok')

if __name__ == "__main__":
    main()