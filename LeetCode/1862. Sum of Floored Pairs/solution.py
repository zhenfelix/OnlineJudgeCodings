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



