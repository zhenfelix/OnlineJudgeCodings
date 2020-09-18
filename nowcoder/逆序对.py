# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
h = list(map(int, input().split(' ')))

cnt = [1]*n 
left = []
for i in range(n-1):
    while left and left[-1] <= h[i]:
        left.pop()
    left.append(h[i])
    cnt[i+1] += len(left)

right = []
for i in range(1,n)[::-1]:
    while right and right[-1] <= h[i]:
        right.pop()
    right.append(h[i])
    cnt[i-1] += len(right)

print(' '.join([str(x) for x in cnt]))


