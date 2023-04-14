import sys
# sys.stdin = open("contests/input","r")
n, k = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
i = n//2
s = 0
cnt = 0
ans = 0
while i < n:
    if arr[i]*(cnt+1)-s-arr[i] > k:
        break
    s += arr[i]
    cnt += 1
    i += 1
print((k-(arr[i-1]*cnt-s))//cnt+arr[i-1])
     

    

