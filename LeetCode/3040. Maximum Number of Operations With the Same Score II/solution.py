class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,j,s):
            if i >= j: return 0
            ans = 0
            if nums[i]+nums[j] == s:
                ans = max(ans,1+dfs(i+1,j-1,s))
            if nums[i]+nums[i+1] == s:
                ans = max(ans,1+dfs(i+2,j,s))
            if nums[j]+nums[j-1] == s:
                ans = max(ans,1+dfs(i,j-2,s))
            return ans 
        n = len(nums)

        return 1+max(dfs(1,n-2,nums[0]+nums[-1]),dfs(2,n-1,nums[0]+nums[1]),dfs(0,n-3,nums[-1]+nums[-2]))