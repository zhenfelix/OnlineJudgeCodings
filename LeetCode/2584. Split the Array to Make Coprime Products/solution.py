class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        left, right = dict(), dict()
        n = len(nums)
        for i in range(n):
            right[nums[i]] = i 
            left[nums[n-1-i]] = n-1-i  
        mx = max(nums)
        delta = [0]*n 
        p = [1]*(mx+1)
        for i in range(2,mx+1):
            if p[i] == 0: continue
            lo, hi = inf, -inf
            for j in range(i,mx+1,i):
                p[j] = 0
                if j not in left: continue
                lo = min(lo, left[j])
                hi = max(hi, right[j])
            if lo > hi: continue
            delta[lo] += 1
            delta[hi] -= 1
        cur = 0
        for i in range(n-1):
            cur += delta[i]
            if cur == 0: return i  
        return -1


class PrimeHelper:
    __slots__ = "_minPrime"  # 每个数的最小质因数

    def __init__(self, maxN: int):
        """预处理 O(nloglogn)"""
        minPrime = list(range(maxN + 1))
        upper = int(maxN**0.5) + 1
        for i in range(2, upper):
            if minPrime[i] < i:
                continue
            for j in range(i * i, maxN + 1, i):
                if minPrime[j] == j:
                    minPrime[j] = i
        self._minPrime = minPrime

    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        return self._minPrime[n] == n

    def getPrimeFactors(self, n: int):
        """求n的质因数分解 O(logn)"""
        pre, f = 1, self._minPrime
        while n > 1:
            m = f[n]
            if m != pre:
                yield m
                pre = m
            n //= m

    def getPrimes(self) -> List[int]:
        return [x for i, x in enumerate(self._minPrime) if i >= 2 and i == x]


作者：FreeYourMind
链接：https://leetcode.cn/problems/split-the-array-to-make-coprime-products/solution/wu-di-de-dai-ma-you-lai-liao-gan-xie-xia-p1ht/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。