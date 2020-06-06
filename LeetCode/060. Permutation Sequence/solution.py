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