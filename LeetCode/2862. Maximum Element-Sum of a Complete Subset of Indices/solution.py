nmax = 10**4+10
mp = dict()
for v in range(1,nmax):
    tmp = v 
    cur = 1
    f = 2
    while f*f <= v:
        cnt = 0
        if v%f == 0:
            while v%f == 0:
                cnt += 1
                v //= f 
        if cnt%2:
            cur *= f 
        f += 1
    if v > 1:
        cur *= v 
    mp[tmp] = cur 
# print(mp)
nmax = 10**4+10
mp = [1]*nmax
prime = [True]*nmax
for f in range(2,nmax):
    if prime[f]:
        for nf in range(f,nmax,f):
            prime[nf] = False 
            cnt = 0
            tmp = nf 
            while nf%f == 0:
                cnt += 1
                nf //= f 
            if cnt%2:
                mp[tmp] *= f 

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = 0
        cc = defaultdict(int)
        for i, v in enumerate(nums):
            i += 1
            cc[mp[i]] += v 
            ans = max(ans, cc[mp[i]])
        return ans 


@cache  # 保存 core(n) 的计算结果，测试用例之间可以复用
def core(n: int) -> int:
    res = 1
    for i in range(2, isqrt(n) + 1):
        e = 0
        while n % i == 0:
            e ^= 1
            n //= i
        if e:
            res *= i
    if n > 1:
        res *= n
    return res

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        s = Counter()
        for i, x in enumerate(nums, 1):
            s[core(i)] += x
        return max(s.values())


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/SwCGEn/view/Ukiom8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        seen = [0]*n 
        for i in range(n):
            if seen[i]: continue
            res = 0
            for j in count(1):
                idx = (i + 1) * j * j - 1
                if idx >= n: break
                res += nums[idx]
                seen[idx] = 1
            ans = max(ans, res)
        return ans

# 作者：小羊肖恩
# 链接：https://leetcode.cn/circle/discuss/SwCGEn/view/TRBVNn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def maximumSum(self, A: List[int]) -> int:
        return max(sum(A[d * x * x - 1]
                       for x in range(1, isqrt(len(A) // d) + 1))
                   for d in range(1, len(A) + 1))


作者：不造轮子
链接：https://leetcode.cn/circle/discuss/SwCGEn/view/L30JPr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。