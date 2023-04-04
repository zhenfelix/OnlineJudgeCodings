nmax = 1005
ps = [1]*nmax
for i in range(2,nmax):
    if not ps[i]: continue
    for j in range(i*2,nmax,i):
        ps[j] = 0
primes = []
for i in range(2,nmax):
    if ps[i]: primes.append(i)


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        pre = -1
        for cur in nums:
            tmp = cur
            for p in primes:
                if p >= cur: break
                if cur-p > pre:
                    tmp = cur-p  
                else:
                    break  
            if tmp <= pre:
                return False
            pre = tmp 
        return True
