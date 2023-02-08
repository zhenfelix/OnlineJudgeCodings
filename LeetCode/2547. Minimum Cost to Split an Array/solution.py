class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def dfs(sz):
            if sz == 0:
                return 0 
            cnt = 0
            cc = Counter()
            ans = inf 
            for i in range(sz)[::-1]:
                if cc[nums[i]] == 1:
                    cnt += 1
                cc[nums[i]] += 1
                if cc[nums[i]] > 1:
                    cnt += 1
                ans = min(ans, dfs(i)+k+cnt)
            return ans 
        return dfs(n)