import sys, heapq
from collections import *
from functools import cmp_to_key

# sys.stdin = open('input.txt', 'r')
n, k = map(int, input().split(' '))
stu = []
for _ in range(n):
    name, height = input().split(' ')
    height = int(height)
    stu.append((name,height))

def cmp(a, b):
    if a[1] < b[1] or (a[1] == b[1] and a[0] > b[0]):
        return -1
    else:
        return 1

stu = sorted(stu, key=cmp_to_key(cmp))
# print(stu)
row = k
while row:
    q = deque()
    if row == k:
        m = n - (n//k)*(k-1)
    else:
        m = n//k
    turn = False
    for _ in range(m):
        if turn:
            q.appendleft(stu.pop()[0])
        else:
            q.append(stu.pop()[0])
        turn = not turn
    row -= 1
    print(' '.join(list(q)))
