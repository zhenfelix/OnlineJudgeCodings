class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1,n+1)]
        fac = [1]
        for i in range(1,n+1):
            fac.append(fac[-1]*i)
        k -= 1
        res = ''
        while n:
            idx = k//fac[n-1]
            res += nums[idx]
            nums = nums[:idx] + nums[idx+1:]
            k %= fac[n-1]
            n -= 1
        return res


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        fac = [1]*(n+1)
        for i in range(1,n+1):
            fac[i] = fac[i-1]*i
        used = [False]*(n+1)
        k -= 1
        for i in range(n)[::-1]:
            cnt = k//fac[i]
            k -= fac[i]*cnt
            x = 1
            while cnt >= 0:
                if not used[x]:
                    cnt -= 1
                if cnt < 0:
                    used[x] = True
                    res.append(x)
                x += 1
        return ''.join(map(str,res))
