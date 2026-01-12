class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        @lru_cache(None)
        def dfs(i,v,flip):
            if i == 0:
                return 0 if nums[i]*flip == v else inf
            if i == 1:
                if nums[0] != nums[1]*flip:
                    return inf 
                return 0 if nums[i]*flip == v else 1
            if nums[i]*flip == v:
                return dfs(i-1,v,1)
            return dfs(i-1,v,-1)+1
        # print(dfs(n-1,1,1),dfs(n-1,-1,1))
        return min(dfs(n-1,1,1),dfs(n-1,-1,1)) <= k
