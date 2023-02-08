class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mx = max(nums)
        presums = [0]*(mx+1)
        cnt = [0]*(mx+1)
        for a in nums:
            cnt[a] += 1
            presums[a] += 1
        for a in range(1,mx+1):
            presums[a] += presums[a-1]
        ans = 0
        MOD =10**9+7
        for x in range(1,mx+1):
            if cnt[x] == 0: continue
            y = x
            while y <= mx:
                ans = (ans+cnt[x]*(presums[min(x+y-1,mx)]-presums[y-1])*y//x)%MOD 
                y += x 
            # ans = (ans-cnt[x])%MOD 
            # print(x,ans)
        return ans 

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        nmax = 100005
        MOD = 10**9+7
        mp = Counter(nums)
        tree = [0]*nmax
        for i in range(1,nmax):
            tree[i] = tree[i-1] + mp[i]
        
        res = 0

        for x in range(1,nmax):
            if tree[x] == tree[x-1]:
                continue
            cnt = 1
            for y in range(x,nmax,x):
                res += (tree[min(y+x-1,nmax-1)]-tree[y-1])*cnt*(tree[x]-tree[x-1])
                res %= MOD
                cnt += 1

        return res 



