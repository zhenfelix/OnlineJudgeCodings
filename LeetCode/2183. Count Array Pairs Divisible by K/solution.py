    def coutPairs(self, A, k):
        cnt = Counter(math.gcd(a, k) for a in A)
        res = 0
        for a in cnt:
            for b in cnt:
                if a <= b and a * b % k == 0:
                    res += cnt[a] * cnt[b] if a < b else cnt[a] * (cnt[a] - 1) // 2
        return res


class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        def gcd(a, b):
            if b == 0:
                return a 
            if a < b:
                return gcd(b, a)
            return gcd(b, a%b)

        cnt = 0
        cc = Counter()
        for i, x in enumerate(nums):
            g = gcd(x, k)
            g = k//g 
            cnt += cc[g]
            q = 1
            # print(i,x,cnt,cc)
            while q*q <= k:
                if k%q == 0:
                    if x%q == 0:
                        cc[q] += 1
                    p = k//q
                    if x%p == 0 and p != q:
                        cc[p] += 1
                q += 1
        return cnt 


class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        N, output = len(nums), 0
        divisors = []
        counter = Counter()
        
        for i in range(1, k + 1):
            if k % i == 0:
                divisors.append(i)
        
        for i in range(0, N):
            remainder = k // math.gcd(k, nums[i])
            output += counter[remainder]
            for divisor in divisors:
                if nums[i] % divisor == 0:
                    counter[divisor] += 1
            
        return output


class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a 
            return gcd(b, a%b)

        cnt = 0
        cc = Counter(nums)
        mx = max(nums)
        mx = max(mx, k)
        for f in range(1,mx+1):
            if k%f:
                continue
            for fs in range(f*2,mx+1,f):
                cc[f] += cc[fs]
        for x in nums:
            g = gcd(x, k)
            g = k//g 
            cnt += cc[g]
        for x in nums:
            if x*x%k == 0:
                cnt -= 1
        return cnt//2


class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a 
            return gcd(b, a%b)

        cnt = 0
        cc = Counter(nums)
        cc2 = Counter()
        mx = max(nums)
        for f in range(1,k+1):
            if f*f > k:
               break
            if k%f:
                continue
            for fs in range(f,mx+1,f):
                cc2[f] += cc[fs]
            f2 = k//f 
            if f2 == f:
                continue
            for fs in range(f2,mx+1,f2):
                cc2[f2] += cc[fs]
        # print(cc2)
        for x in nums:
            g = gcd(x, k)
            g = k//g 
            cnt += cc2[g]
            if (x*x)%k == 0:
                cnt -= 1
        return cnt//2