from collections import *
from functools import *
from heapq import * 
import sys 
from bisect import * 



def solve():
    s = input()
    s = [ch for ch in s if ch != ' ']
    n = len(s)
    def calc(st, ops):
        if len(st) == 1:
            return st[0]
        cur = [st[0]]
        for op, v in zip(ops,st[1:]):
            if op == '*':
                cur[-1] *= v 
            else:
                cur.append(v)
        return sum(cur)

    def check(exp):
        # print(exp)
        st, ops = [], []
        val = 0
        for i, ch in enumerate(exp):

            if ch not in ['=','+','*']:
                val = val*10+int(ch)
            if ch in ['=','+','*'] or i == len(exp)-1:
                st.append(val)
                val = 0
            if ch in ['+','*']:
                ops.append(ch)

            if ch == '=':
                left = calc(st, ops)
                st, ops = [], []
            if i == len(exp)-1:
                right = calc(st,ops)
        return left == right
    for i in range(n+1):
        for v in range(10):
            if check(s[:i]+[str(v)]+s[i:]):
                return "YES"
    return  "NO"

sys.stdin = open('duipai/data.in', 'r')
# print(solve())
t = int(input())
for _ in range(t):
    print(solve())
# solve()