# import sys
# sys.stdin = open("input.txt", "r")

import heapq
n, L = list(map(int, input().split(' ')))
arr = []
for i in range(n):
    a, b = list(map(int, input().split(' ')))
    arr.append((a,b))
heapq.heapify(arr)
cur, cnt = 0, 0
while arr and cur < L:
    nxt = cur
    while arr and arr[0][0] <= cur:
        a, b = heapq.heappop(arr)
        nxt = max(nxt,b)
    if nxt <= cur: break 
    cur = nxt
    cnt += 1

if cur >= L:
    print(cnt)
else:
    print(-1)
