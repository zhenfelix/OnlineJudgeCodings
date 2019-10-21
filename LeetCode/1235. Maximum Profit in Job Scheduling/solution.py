class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        nums = [(startTime[i],endTime[i],profit[i]) for i in range(n)]
        nums = sorted(nums)
        def  dfs(cur):
            if cur in memo:
                return memo[cur]
            if cur == n:
                memo[cur] = 0
                return memo[cur]
            res = dfs(cur+1)
            end = nums[cur][1]
            lo, hi = cur+1, n-1
            while lo <= hi:
                mid = (lo+hi)//2
                if nums[mid][0] >= end:
                    hi = mid-1
                else:
                    lo = mid+1
            res = max(res,nums[cur][2]+dfs(lo))
            memo[cur] = res
            return res
        memo = {}
        return dfs(0)

