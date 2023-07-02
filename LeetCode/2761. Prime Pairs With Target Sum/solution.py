class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        primes = [1]*(n+1)
        primes[0] = primes[1] = 0
        for f in range(2,n+1):
            if primes[f] == 0: continue
            for nf in range(f*f,n+1,f):
                primes[nf] = 0
        ans = []
        for a in range(2,n+1):
            if n-a < a: break
            if primes[a] and primes[n-a]:
                ans.append([a,n-a])
        return ans 

MX = 10 ** 6 + 1
primes = []
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        ans = []
        for x in primes:
            y = n - x
            if y < x:
                break
            if is_prime[y]:
                ans.append([x, y])
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/501Jzp/view/uQITil/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。