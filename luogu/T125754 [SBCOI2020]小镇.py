# https://www.luogu.com.cn/problem/T125754?contestId=27163
# https://www.luogu.com.cn/blog/12cow/SBCOI2020

import sys, heapq
from collections import *




# sys.stdin = open('input.txt', 'r')
n, k = map(int, input().split(' '))
house = set()

for i in range(k):
    x, y = map(int, input().split(' '))
    house.add((x,y))
cnt = 0
for x, y in house:
    for dx, dy in [(0,-1),(0,1),(1,0),(-1,0)]:
        if (x+dx,y+dy) in house: cnt += 1
print(cnt//2)
