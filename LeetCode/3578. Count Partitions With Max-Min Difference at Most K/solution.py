class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        dp = [0]*(n+1)
        ss = [0]*(n+1)
        dp[-1] = 1
        ss[-1] = 1
        j = 0
        mi = deque()
        mx = deque()
        for i in range(n):
            while mi and nums[mi[-1]] >= nums[i]:
                mi.pop()
            mi.append(i)
            while mx and nums[mx[-1]] <= nums[i]:
                mx.pop()
            mx.append(i)
            while nums[mx[0]]-nums[mi[0]] > k:
                if j == mx[0]:
                    mx.popleft()
                if j == mi[0]:
                    mi.popleft()
                j += 1
            dp[i] = (ss[i-1]-ss[j-2])%MOD 
            ss[i] = (ss[i-1]+dp[i])%MOD
            # print(j,i,dp)
            # print(mi,mx)
        return dp[n-1]

