class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n = len(nums)
        nums.sort()
        s = ans = 0
        for a in nums:
            ans += a*a*(a+s)
            ans %= MOD 
            s = s*2+a 
            s %= MOD 
        return ans 


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n = len(nums)
        f = [1]*(n+1)
        for i in range(1,n+1):
            f[i] = f[i-1]*2  
            f[i] %= MOD 
        def quickmul(a, q):
            b = 1
            while q:
                if q&1:
                    b = (b*a)%MOD 
                q >>= 1
                a = (a*a)%MOD 
            return b 

        invf = [1]*(n+1)
        invf[n] = quickmul(f[n],MOD-2)
        for i in range(n)[::-1]:
            invf[i] = 2*invf[i+1]
            invf[i] %= MOD
        # print(f,invf)
        s = 0
        ans = 0
        nums.sort()
        
        for i in range(n):
            x = nums[i]
            ans += x*x*x
            ans += s*f[i]*x*x
            ans %= MOD 
            s += x*invf[i+1]
            s %= MOD 
        return ans 