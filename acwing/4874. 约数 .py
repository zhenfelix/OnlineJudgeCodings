n = int(input())
arr = list(map(int, input().split()))
nmax = 10**6+10
prime = [True]*nmax
prime[0] = prime[1] = False  
for i in range(nmax):
    if not prime[i]: continue
    for j in range(i*i, nmax, i):
        prime[j] = False

def check(x):
    lo, hi = 1, x
    while lo <= hi:
        mid = (lo+hi)//2
        if mid*mid == x:
            return prime[mid]
        elif mid*mid < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
for a in arr:
    if check(a):
        print("YES")
    else:
        print("NO")
