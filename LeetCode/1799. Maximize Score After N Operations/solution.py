class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)//2
        def gcd(a, b):
            a, b = max(a,b), min(a,b)
            if b == 0:
                return a
            return gcd(b, a%b)

        def dfs(cur,idx):
            # print(cur,idx)
            if cur in memo:
                return memo[cur]
            if idx == n:
                return 0
            res = 0
            # print(cur,idx,res)
            for i in range(2*n):
                if cur & (1<<i):
                    for j in range(i+1,2*n):
                        if cur & (1<<j):
                            tmp = gcd(nums[i],nums[j])
                            # print(i,j,nums[i],nums[j],tmp)
                            res = max(res, (idx+1)*tmp+dfs(cur^(1<<i)^(1<<j), idx+1))
            # print(cur,idx,res)
            memo[cur] = res
            return res 

        ans = dfs((1<<(2*n))-1,0)
        # print(memo)
        return ans
