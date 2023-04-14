
import sys 
# sys.stdin = open("contests/input","r")

n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
visited = [0]*n 
nxt, pre = [-1]*n, [-1]*n 
for i in range(n-1): nxt[i] = i+1
for i in range(1,n)[::-1]: pre[i] = i-1
ans = [0]*n 
flag = 1
mp = {v-1:i for i, v in enumerate(arr)}
for i in range(n)[::-1]:
    j = mp[i]
    if visited[j]: continue
    visited[j] = flag
    left, right = -1, -1
    cur = nxt[j]
    for _ in range(k):
        if cur == -1: break 
        visited[cur] = flag
        cur = nxt[cur]
    right = cur 
    cur = pre[j]
    for _ in range(k):
        if cur == -1: break
        visited[cur] = flag
        cur = pre[cur]
    left = cur 
    if left != -1: nxt[left] = right
    if right != -1: pre[right] = left
    flag = 3-flag
print(''.join(map(str,visited)))