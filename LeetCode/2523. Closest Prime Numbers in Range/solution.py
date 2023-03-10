nmax = 10**6+10
primes = [True]*nmax
for i in range(2,nmax):
    if not primes[i]: continue
    for j in range(i*i,nmax,i):
        primes[j] = False
primes[0] = primes[1] = False

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = [i for i in range(left,right+1) if primes[i]]
        if len(arr) < 2:
            return [-1,-1]
        return min([[a,b] for a, b in zip(arr[:-1],arr[1:])], key = lambda x: x[-1]-x[0])